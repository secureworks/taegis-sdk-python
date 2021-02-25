from dataclasses import dataclass, field

from dateutil.parser import *
from dateutil.relativedelta import *
from datetime import datetime, timedelta

from taegis_sdk_python.utils import do_parse_time_to_utc_epoch, duration_string


@dataclass
class Time:
    date: str
    utc: datetime = field(init=False)
    local: datetime = field(init=False)
    epoch: str = field(init=False)
    diff: relativedelta = field(init=False)
    timestamp: int = field(init=False)

    @staticmethod
    def convert(date: str):
        return Time(date)

    def __post_init__(self):
        if self.date:
            e, d = do_parse_time_to_utc_epoch(self.date)
            setattr(self, "diff", d)
            setattr(self, "epoch", e)
            dt = parse(self.date)
            setattr(self, "utc", dt)
            setattr(self, "timestamp", dt.timestamp())
            offset = (
                datetime.fromtimestamp(dt.timestamp())
                - datetime.utcfromtimestamp(dt.timestamp())
            )
            setattr(self, "local", dt + offset)

    def __str__(self):
        return self.date

    def __repr__(self):
        return f'{{id: "{self.date}"}}'


@dataclass
class Epoch:
    duration: int
    duration_str: str = field(init=False)

    @staticmethod
    def convert(duration: int):
        return Epoch(duration=duration)

    def __post_init__(self):
        if self.duration:
            duration = timedelta(seconds=self.duration)
            setattr(self, "duration_str", duration_string(duration))
