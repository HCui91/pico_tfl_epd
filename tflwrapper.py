# Python
"""A very simple wrapper for the TFL API.

This module provides a simple wrapper for the TFL API. It allows for testing
the connection to the API, getting the status of a given line, and getting
arrival predictions for a given line and station.

@Author: HCui91
@Repo: https://github.com/HCui91/pico_tfl_departure_board
"""

import urequests
import ujson
import gc


def test_tfl_connection(app_key: str) -> bool | int:
    """
    Test the connection to the TFL API.

    Args:
        app_key (str): The TFL API app key.

    Returns:
        bool or int: True if the connection is successful, otherwise status code.
    """
    url = f"https://api.tfl.gov.uk/Line/Meta/Modes?app_key={app_key}"
    response = None
    try:
        response = urequests.get(url)
        return True if response.status_code == 200 else response.status_code
    except Exception as e:
        return False
    finally:
        if response:
            response.close()
        gc.collect()


def _fetch_status(app_key: str, line: str, short: bool = True) -> str:
    """
    Get the status of a given line.
    """
    url = f"https://api.tfl.gov.uk/Line/{line}/Status?app_key={app_key}"
    response = None
    data = None
    try:
        response = urequests.get(url)
        data = response.json()
        status = str(data[0]['lineStatuses'][0]['statusSeverityDescription'])
        if short:
            status = "Good" if status == "Good Service" else status
        return status
    except Exception as e:
        return "Error"
    finally:
        if response:
            response.close()
        data = None
        gc.collect()


def _fetch_arrivals(app_key: str, line: str, station_id: str, direction: str = "all", sort: bool = True) -> tuple[list[str], list[int], list[str]]:
    """
    Get arrival predictions for a given line and station.
    """
    url = f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{station_id}?direction=all&app_key={app_key}"
    response = None
    data = None
    try:
        response = urequests.get(url)
        data = response.json()

        platform_number = []
        time_to_station = []
        destinations = []

        for arrival in data:
            platform_name = arrival['platformName'].split()
            if direction != "all" and platform_name[0] != direction:
                continue
            platform_number.append(str(platform_name[-1]))
            time_to_station.append(int(arrival['timeToStation']))
            destinations.append(str(arrival['towards']))

        if sort and time_to_station:
            time_to_station, platform_number, destinations = zip(
                *sorted(zip(time_to_station, platform_number, destinations))
            )
        return list(platform_number), list(time_to_station), list(destinations)
    except Exception as e:
        return [], [], []
    finally:
        if response:
            response.close()
        data = None
        gc.collect()


def fetch_status(app_key: str, lines: list[str], short: bool = True) -> list[str]:
    """
    Get the status of multiple lines.
    """
    results = []
    for line in lines:
        try:
            results.append(_fetch_status(app_key, line, short=short))
        except:
            results.append("Error")
    return results


def fetch_arrivals(app_key: str, lines: list[str], station_id: str, direction: str = "all", sort: bool = True) -> tuple[list[str], list[int], list[str]]:
    """
    Get arrival predictions for multiple lines at a given station.
    """
    platform_number = []
    time_to_station = []
    towards = []
    for line in lines:
        try:
            pn, ts, tw = _fetch_arrivals(app_key, line, station_id, direction=direction, sort=False)
            platform_number += pn
            time_to_station += ts
            towards += tw
        except:
            continue

    if sort and time_to_station:
        time_to_station, platform_number, towards = zip(
            *sorted(zip(time_to_station, platform_number, towards))
        )
        return list(platform_number), list(time_to_station), list(towards)
    return platform_number, time_to_station, towards