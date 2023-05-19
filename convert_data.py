from datetime import datetime
import pytz
from tzlocal import get_localzone


def current_local_datetime() -> datetime:
    return datetime.now(get_localzone())


def convert_unix_timestamp_to_local_datetime(timestamp: float) -> datetime:
    dtime = datetime.fromtimestamp(timestamp, get_localzone())
    return dtime


def current_utc_datetime() -> datetime:
    return datetime.now(pytz.utc)


def convert_datetime_to_unix_timestamp(dtime: datetime) -> float:
    unix_timestamp = dtime.astimezone(pytz.utc).timestamp()
    return unix_timestamp


def convert_unix_timestamp_to_utc_datetime(timestamp: float) -> datetime:
    dtime = datetime.fromtimestamp(timestamp, pytz.utc)
    return dtime


def convert_datetime_to_utc_string(dtime: datetime) -> str:
    dtime_str = dtime.strftime('%Y-%m-%dT%H:%M:%SZ')
    return dtime_str