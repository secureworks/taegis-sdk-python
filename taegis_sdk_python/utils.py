import dataclasses
import inspect
import logging
from datetime import datetime
from typing import Any, Dict

from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import os

import stringcase
from dateutil import tz
from dateutil.parser import *
from dateutil.relativedelta import *

logger = logging.getLogger("query-builder.utils")


def get_args_from_frame(frame) -> Dict[str, Any]:
    args, _, _, values = inspect.getargvalues(frame)
    values_map = {}
    args.pop(0)
    for arg in args:
        if hasattr(values[arg], "__dataclass_fields__"):
            asdict = dataclasses.asdict(values[arg])
            from operator import itemgetter
            asdict = dict(filter(itemgetter(1), asdict.items()))
            asdict = dict((stringcase.camelcase(k), v) for k, v in asdict.items())
            values_map.update(asdict)
        elif values[arg] is not None:
            values_map[stringcase.camelcase(arg)] = values[arg]
    return values_map


def do_parse_time_to_utc_epoch(utc_str: str):
    tod = datetime.now(tz.UTC)
    if isinstance(utc_str, str):
        utc_field = parse(utc_str)
    else:
        utc_field = utc_str
    diff = relativedelta(utc_field, tod)
    years = months = days = hours = ""
    if abs(diff.years) > 0:
        years = f"{abs(diff.years)} years, "
    if abs(diff.months) > 0:
        months = f"{abs(diff.months)} months, "
    if abs(diff.days) > 0:
        days = f"{abs(diff.days)} days, "
    if abs(diff.hours) > 0:
        hours = f"{abs(diff.days)} hours, "
    epoch_field = (
        f'{years}{months}{days}{hours}{abs(diff.minutes)} minutes '
        f'and {abs(diff.seconds)} secs ago.')
    return epoch_field, diff


def duration_microseconds(delta):
    return (24 * 60 * 60 * delta.days + delta.seconds) * 1000000 + delta.microseconds


def duration_string(duration):
    """Version of str(timedelta) which is not English specific."""
    days, hours, minutes, seconds, microseconds = _get_duration_components(duration)

    string = '{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)
    if days:
        string = '{} '.format(days) + string
    if microseconds:
        string += '.{:06d}'.format(microseconds)

    return string


def _get_duration_components(duration):
    days = duration.days
    seconds = duration.seconds
    microseconds = duration.microseconds

    minutes = seconds // 60
    seconds %= 60

    hours = minutes // 60
    minutes %= 60

    return days, hours, minutes, seconds, microseconds


def is_valid_value(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return True if value else False
    return True


def get_token():
    """
    Get tokne url based on CLIENT_ID and CLIENT_SECRET values
    :return: the token for the schema and execute queries
    """
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')
    client = BackendApplicationClient(client_id=client_id)
    oauth_client = OAuth2Session(client=client)
    token = oauth_client.fetch_token(token_url='https://api.ctpx.secureworks.com/auth/api/v2/auth/token',
                                     client_id=client_id,
                                     client_secret=client_secret)
    return token


__all__ = [
    "duration_string",
    "is_valid_value",
    "duration_string",
    "do_parse_time_to_utc_epoch",
    "get_args_from_frame",
    "get_token"
]
