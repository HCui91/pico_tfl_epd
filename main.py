import time
import gc
from writer import Writer
from Pico_ePaper_2in9 import EPD_2in9_Landscape
import robotosemibold24 as font
from wlan import WiFi
from synctime import sync_time, localtime
from tflwrapper import test_tfl_connection, fetch_status
from weather import fetch_weather, test_weather_connection, parse_weather_endpoint
from configs import TFL_APP_KEY, WIFI_SSID, WIFI_PASSWORD, WEATHER_API_KEY, WEATHER_LAT, WEATHER_LON, LINE_IDS, LINE_TITLES
from logging import debug, info, warning, error, trim_log_file

class TFLDisplay:
    def __init__(self):
        # Initialize the ePaper display and writer
        self.screen = EPD_2in9_Landscape()
        self.writer = Writer(self.screen, font, header_height=0, line_space=0)
        self.writer.invert = True
        self.writer.bgcolor, self.writer.fgcolor = 1, 0
        Writer.set_textpos(self.screen, 0, 0)
        
        # Initialize WiFi and weather endpoint
        self.wifi = WiFi()
        self.weather_endpoint = parse_weather_endpoint(WEATHER_API_KEY, WEATHER_LAT, WEATHER_LON)

    def initialise(self):
        # Connect to WiFi
        self.wifi_connected = self.wifi.connect(WIFI_SSID, WIFI_PASSWORD, timeout=30)
        if self.wifi_connected:
            info(f"WiFi connected, IP address: {self.wifi.wlan.ifconfig()[0]}")
        else:
            error("WiFi connection failed")
            return False
        
        # Sync time
        sync_time(max_try=1)

        # Test TFL API connection
        tfl_connected = test_tfl_connection(TFL_APP_KEY)
        info(f"TFL API: {tfl_connected}")
        if not tfl_connected:
            return False

        # Test OpenWeather API connection
        weather_connected = test_weather_connection(self.weather_endpoint)
        info(f"Weather API: {weather_connected}")
        if not weather_connected:
            return False

        # Perform garbage collection and return True if all initializations are successful
        time.sleep(1)
        gc.collect()
        debug(f"Memory available: {gc.mem_free()}")
        return True

    def main(self):
        # Clear the screen and display the line status board
        self.screen.clear()
        self._line_status_board(LINE_IDS, LINE_TITLES)

    def _line_status_board(self, lines: list[str], line_titles: list[str]):
        # Determine the number of lines to display
        num_lines = min(self.writer.get_num_lines() - 2, len(lines))
        if num_lines < len(lines):
            warning(f"Too many lines to display, only the first {num_lines} will be shown")
        lines = lines[:num_lines]
        line_titles = line_titles[:num_lines]

        # Initialize variables for tracking old statuses and refresh needs
        old_line_status = [""] * num_lines
        old_weather = ""
        old_temperature = "*C"
        need_refresh = False
        last_fetch_time = 0
        last_full_refresh_time = 0
        last_minute = -1
        last_time_sync = time.time()
        running_dot = 0

        while True:
            current_time = time.time()
            
            # Fetch weather and line status every 90 seconds
            if current_time - last_fetch_time > 90:
                info(f"Fetching weather and line status after {current_time - last_fetch_time} seconds")
                line_status = fetch_status(TFL_APP_KEY, lines, short=True)
                debug(f"Line status: {line_status}")
                weather, temperature = fetch_weather(self.weather_endpoint)
                debug(f"Weather: {weather}, temperature: {temperature}")
                last_fetch_time = current_time

                # Determine if a refresh is needed
                need_refresh = (
                    weather != old_weather or
                    temperature != old_temperature or
                    any(line_status[i] != old_line_status[i] for i in range(num_lines))
                )
                info(f"Fetch done, need_refresh={need_refresh}")

            # Force a full refresh every hour
            if current_time - last_full_refresh_time > 3600:
                info("Forcing full refresh after 1 hour")
                need_refresh = True
                trim_log_file("main.log", 1000)

            # Sync time every day
            if current_time - last_time_sync > 86400:
                info("Forcing time sync after 1 day")
                sync_time(max_try=0)
                last_time_sync = current_time

            # Perform a full refresh if needed and more than 3 minutes have passed since the last full refresh
            if need_refresh and current_time - last_full_refresh_time > 180:
                info(f"Full refreshing after {current_time - last_full_refresh_time} seconds")
                self.screen.fill(0xff)
                self.writer.mytext_both_side(weather, temperature, 0)
                for i in range(num_lines):
                    self.writer.mytext_both_side(line_titles[i], line_status[i], i + 1)
                self.writer.mytext_both_side(
                    f"{localtime()[0]}-{localtime()[1]:02d}-{localtime()[2]:02d}",
                    f"{localtime()[3]:02d}:{localtime()[4]:02d}", num_lines + 1
                )
                self.screen.show(1)

                # Update old statuses and reset refresh flags
                need_refresh = False
                old_line_status = line_status
                old_weather = weather
                old_temperature = temperature
                last_minute = localtime()[4]
                last_full_refresh_time = current_time
                info("Full refresh done")

            # Perform a partial refresh of the clock every minute
            if localtime()[4] != last_minute:
                info("Partial refreshing clock")
                last_minute = localtime()[4]
                self.writer.clear_line(num_lines + 1)
                self.writer.mytext_both_side(
                    f"{localtime()[0]}-{localtime()[1]:02d}-{localtime()[2]:02d}",
                    f"{localtime()[3]:02d}:{localtime()[4]:02d}", num_lines + 1
                )
                self.screen.show(2)
                info("Partial refresh done")
                gc.collect()
                debug(f"Memory available: {gc.mem_free()}")

            # Update the running dot animation
            running_dot_pos = running_dot % 5
            self.screen.fill_rect(287, 125, 9, 3, 0xff)
            if running_dot_pos >= 3:
                self.screen.fill_rect(287 + 3 * (4 - running_dot_pos), 125, 3, 3, 0x00)
            else:
                self.screen.fill_rect(287 + 3 * running_dot_pos, 125, 3, 3, 0x00)
            self.screen.show(2)
            running_dot += 1
            time.sleep(1)

if __name__ == "__main__":
    while True:
        info("Start main loop")
        gc.collect()
        debug(f"Memory available: {gc.mem_free()}")
        trim_log_file("main.log", 1000)
        app = TFLDisplay()
        if app.initialise():
            info("Initialisation successful")
            app.main()
            info("Exit from the main menu")
        else:
            info("Initialisation failed")
        info("Restart in 5 seconds")
        gc.collect()
        time.sleep(5)
