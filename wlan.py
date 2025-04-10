import time
import network
import ubinascii


class WiFi:

    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)
        self.wlan.config(pm=0xa11140)  # disable power-saving
        mac = ubinascii.hexlify(self.wlan.config('mac'), ':').decode()
        print(f"MAC = {mac}")

    def connect(self, ssid, password, timeout=10):
        self.wlan.connect(ssid, password)

        # Wait for connect or fail
        while timeout > 0:
            if self.wlan.status() < 0 or self.wlan.status() >= 3:
                break
            timeout -= 1
            print('waiting for connection...')
            time.sleep(1)

        # Handle connection error
        if self.wlan.status() != 3:
            print(f"wlan.status() = {self.wlan.status()}")
            return False
        else:
            print(f"{ssid} connected")
            print(f"ip = {self.wlan.ifconfig()[0]}")
            return True

    def disconnect(self):
        self.wlan.disconnect()
        print('wlan disconnected')
