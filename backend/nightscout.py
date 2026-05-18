#nightscout data 
import requests
from datetime import datetime

from nightscout_secrets import nightscout_url

def converted_count(time_from: str, time_until: str) -> int:
    """
    Works out how many blood sugars are contained within timeframe.
    Nightscout API defaults to displaying 10 data points unless count=x is specified.
    Timeframe is converted from str to datetime object to work out total time.
    Duration returns H:M:S. 
    Converted_count converts to seconds. 
    Divide by 300 to get 5 minutes per CGM reading. 
    Add 10 as buffer.
    """
    fmt = "%Y-%m-%dT%H:%M:%SZ"
    start, until = (
        datetime.strptime(time_from, fmt),
        datetime.strptime(time_until, fmt)
    )
    duration = until - start 
    converted_count = int((duration.total_seconds() / 300) + 10) 
    return converted_count

def nightscout_data(time_from: str, time_until: str) -> dict:
    path = "api/v1/entries/sgv.json"
    url = nightscout_url
    count = converted_count(time_from, time_until)
    params = {
        "count": count,
        "find[dateString][$gte]": time_from,
        "find[dateString][$lt]": time_until,
    }
    response = requests.get(f"{url}/{path}", params=params)
    data = response.json()
    final_data = []
    for each in range(len(data)):
        final_data.append(
        f"""Glucose: {data[each]["glucose"]/18:.1f}, 
        Time: {data[each]["dateString"]}, 
        Direction: {data[each]["direction"]}""")
    return final_data
