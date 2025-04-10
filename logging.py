import sys
import time
import os

CRITICAL = const(50)
ERROR = const(40)
WARNING = const(30)
INFO = const(20)
DEBUG = const(10)
NOTSET = const(0)

_level_str = {
    CRITICAL: "CRITICAL",
    ERROR: "ERROR",
    WARNING: "WARNING",
    INFO: "INFO",
    DEBUG: "DEBUG"
}

_stream = sys.stderr  # default output
_filename = "main.log"  # overrides stream
_level = DEBUG  # ignore messages which are less severe
_format = "%(asctime)s\t%(levelname)s\t%(message)s"  # default message format
_loggers = dict()


class Logger:

    def __init__(self, name):
        self.name = name
        self.level = _level
        self.start_ms = time.ticks_ms()

    def log(self, level, message, *args):
        if level < self.level:
            return

        try:
            if args:
                message = message % args

            record = dict()
            record["levelname"] = _level_str.get(level, str(level))
            record["level"] = level
            record["message"] = message
            record["name"] = self.name
            tm = time.localtime()
            record["asctime"] = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}" \
                .format(tm[0], tm[1], tm[2], tm[3], tm[4], tm[5])
            record["chrono"] = "{:f}".format(time.ticks_diff(time.ticks_ms(),self.start_ms)/1000)

            log_str = _format % record + "\n"
            
            _ = _stream.write(log_str)
            if _filename is not None:
                with open(_filename, "a") as fp:
                    fp.write(log_str)

        except Exception as e:
            print("--- Logging Error ---")
            print(repr(e))
            print("Message: '" + message + "'")
            print("Arguments:", args)
            print("Format String: '" + _format + "'")
            raise e

    def setLevel(self, level):
        self.level = level

    def debug(self, message, *args):
        self.log(DEBUG, message, *args)

    def info(self, message, *args):
        self.log(INFO, message, *args)

    def warning(self, message, *args):
        self.log(WARNING, message, *args)

    def error(self, message, *args):
        self.log(ERROR, message, *args)

    def critical(self, message, *args):
        self.log(CRITICAL, message, *args)

    def exception(self, exception, message, *args):
        self.log(ERROR, message, *args)

        if _filename is None:
            sys.print_exception(exception, _stream)
        else:
            with open(_filename, "a") as fp:
                sys.print_exception(exception, fp)


def getLogger(name="root"):
    if name not in _loggers:
        _loggers[name] = Logger(name)
    return _loggers[name]


def basicConfig(level=INFO, filename=None, filemode='a', format=None):
    global _filename, _level, _format
    _filename = filename
    _level = level
    if format is not None:
        _format = format

    if filename is not None and filemode != "a":
        with open(filename, "w"):
            pass  # clear log file


def setLevel(level):
    getLogger().setLevel(level)


def debug(message, *args):
    getLogger().debug(message, *args)


def info(message, *args):
    getLogger().info(message, *args)


def warning(message, *args):
    getLogger().warning(message, *args)


def error(message, *args):
    getLogger().error(message, *args)


def critical(message, *args):
    getLogger().critical(message, *args)


def exception(exception, message, *args):
    getLogger().exception(exception, message, *args)


def trim_log_file(file_path, max_lines=1000):
    # determine the number of lines in the file
    n_lines = 0
    with open(file_path, "r") as f:
        for line in f:
            n_lines += 1
    if n_lines <= max_lines:
        info(f"Trimming {file_path} not needed, {n_lines} lines")
        return
    start_line = n_lines - max_lines
    temp_file_path = file_path + ".tmp"
    info(f"Trimming {file_path} from {n_lines} to {max_lines} lines")
    with open(file_path, "r") as f_in, open(temp_file_path, "w") as f_out:
        for i, line in enumerate(f_in):
            if i >= start_line:
                f_out.write(line)
    os.remove(file_path)
    os.rename(temp_file_path, file_path)
    info(f"Trimming {file_path} done")

if __name__ == "__main__":
    info("This is logging.py. Showing log file content:")
    with open(_filename, "r") as f:
        for line in f:
            print(line.strip())