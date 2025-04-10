import ntptime
import time

from configs import NTP_SERVER, TZ_OFFSET, BST

def march_october_last_sunday(year: int, month: int):
    """Find the last Sunday of March or October in a given year.

    Parameters
    ----------
    year : int
        The year to check.
    month : int
        The month (3 for March, 10 for October).

    Returns
    -------
    int
        The day of the month of the last Sunday.
    """
    for day in range(31, 24, -1):
        temp = time.mktime((year, month, day, 0, 0, 0, 0, 0))
        wd = time.localtime(temp)[6]  # weekday
        if wd == 6:  # Sunday
            return day
    return 31  # fallback, shouldn't happen

def localtime(tz_offset=TZ_OFFSET, use_bst=BST):
    """localtime wrapper to handle timezone and BST.

    Parameters
    ----------
    tz_offset : int
        The timezone offset in hours. Default from configs.py TZ_OFFSET variable.
    use_bst : bool
        Whether to use British Summer Time (BST). If True, tz_offset is ignored and return time is in GMT or BST only. 
        Default from configs.py BST variable.
    
    Returns
    -------
    time.struct_time
        The local time in tuple format `(year, month, mday, hour, minute, second, weekday, yearday)`.

    """
    if use_bst:
        year, month, mday, hour, minute, second, weekday, yearday = time.localtime(time.time())  # local time in GMT

        # Determine if we are in BST
        in_bst = False
        if 3 < month < 10:
            in_bst = True
        elif month == 3:
            last_sun = march_october_last_sunday(year, 3)
            if mday > last_sun or (mday == last_sun and hour >= 1):
                in_bst = True
        elif month == 10:
            last_sun = march_october_last_sunday(year, 10)
            if mday < last_sun or (mday == last_sun and hour < 1):
                in_bst = True
    
        if in_bst:
            # BST is active, add 1 hour to GMT
            return time.localtime(time.time() + 3600)
        else:
            # BST is not active, return GMT
            return time.localtime(time.time())
    else:
        return time.localtime(time.time() + tz_offset * 3600)


def sync_time(max_try=3):
    print(f"Time before sync: {time.localtime()}")
    ntptime.host = NTP_SERVER
    tries = 0
    while tries < max_try:
        # ntp throws an error if it does not need to sync, so we can ignore the exception
        try:
            ntptime.settime()
        except Exception as e:
            print(f"{e}, try {tries}/{max_try}")
            print(f"Time: {time.localtime()}")
            tries += 1
            time.sleep(0.5)
            continue
    print(f"Time after sync: {time.localtime()} after {tries} tries")
    return time.localtime()
