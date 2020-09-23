# @Time    : 2018/9/10
# @Author  : Giles
# @Email   : yangjuntao@joinquant.com
from datetime import datetime, timedelta
import time
from common import custom_exception


datetime_formats = [
                    "%Y-%m-%d %H:%M:%SZ",
                    "%Y-%m-%d %H:%M:%S",
                    "%Y-%m-%d %H:%M:%S%z",
                    "%Y-%m-%d %H:%M:%S.%f",
                    "%Y-%m-%d %H:%M:%S %f",
                    "%Y-%m-%d %H:%M:%S%Z",
                    "%c",
                    "%s",
                    "%Y-%m-%d",
                    # YMD other than ISO
                    "%Y%m%d",
                    "%Y.%m.%d",
                    # Popular MDY formats
                    "%m/%d/%Y",
                    "%m/%d/%y",
                    # DMY with full year
                    "%d %m %Y",
                    "%d-%m-%Y",
                    "%d/%m/%Y",
                    "%d/%m %Y",
                    "%d.%m.%Y",
                    "%d. %m. %Y",
                    "%d %b %Y",
                    "%d %B %Y",
                    "%d. %b %Y",
                    "%d. %B %Y",
                    # MDY with full year
                    "%b %d %Y",
                    "%b %dst %Y",
                    "%b %dnd %Y",
                    "%b %drd %Y",
                    "%b %dth %Y",
                    "%b %d, %Y",
                    "%b %dst, %Y",
                    "%b %dnd, %Y",
                    "%b %drd, %Y",
                    "%b %dth, %Y",
                    "%B %d %Y",
                    "%B %dst %Y",
                    "%B %dnd %Y",
                    "%B %drd %Y",
                    "%B %dth %Y",
                    "%B %d, %Y",
                    "%B %dst, %Y",
                    "%B %dnd, %Y",
                    "%B %drd, %Y",
                    "%B %dth, %Y",
                    # DMY with 2-digit year
                    "%d %m %y",
                    "%d-%m-%y",
                    "%d/%m/%y",
                    "%d/%m-%y",
                    "%d.%m.%y",
                    "%d. %m. %y",
                    "%d %b %y",
                    "%d %B %y",
                    "%d. %b %y",
                    "%d. %B %y",
                    # MDY with 2-digit year
                    "%b %dst %y",
                    "%b %dnd %y",
                    "%b %drd %y",
                    "%b %dth %y",
                    "%B %dst %y",
                    "%B %dnd %y",
                    "%B %drd %y",
                    "%B %dth %y"
]


class HumanDateTime(object):
    def __init__(self, time_object=None):
        self._datetime = None
        if not time_object:
            time_object = datetime.now()
        time_object = str(time_object)
        try:
            time_object = float(time_object)
            self.parse_time(time_object)
        except:
            self.parse_time_str(time_object)

    def parse_time(self, time_object):
        if len(str(int(time_object))) == 10:
            self._datetime = datetime.fromtimestamp(time_object)
        elif len(str(int(time_object))) == 13:
            self._datetime = datetime.fromtimestamp(time_object / 1000.0)
        else:
            raise custom_exception.TimeStampParseError

    def parse_time_str(self, time_object):
        for date in datetime_formats:
            try:
                self._datetime = datetime.strptime(time_object, date)
                break
            except:
                continue
        if not self._datetime:
            raise custom_exception.TimeStampParseError

    @property
    def time_stamp_second(self):
        return int(time.mktime(self._datetime.timetuple()))

    @property
    def time_stamp_microsecond(self):
        return int(time.mktime(self._datetime.timetuple()) * 1e3 + self._datetime.microsecond / 1e3)

    def add(self, days=0, weeks=0, hours=0, minutes=0, seconds=0):
        return self.__class__(str(self._datetime + timedelta(days=days, weeks=weeks, hours=hours, minutes=minutes, seconds=seconds)))

    def sub(self, days=0, weeks=0, hours=0, minutes=0, seconds=0):
        return self.__class__(str(self._datetime + timedelta(days=days, weeks=weeks, hours=hours, minutes=minutes, seconds=seconds)))

    def add_weeks(self, week):
        return self.add(weeks=week)

    def sub_weeks(self, week):
        return self.sub(weeks=week)

    def add_days(self, day):
        return self.add(days=day)

    def sub_days(self, day):
        return self.sub(days=day)

    def add_hours(self, hour):
        return self.add(hours=hour)

    def sub_hours(self, hour):
        return self.sub(hours=hour)

    def add_minutes(self, minute):
        return self.add(minutes=minute)

    def sub_minutes(self, minute):
        return self.sub(minutes=minute)

    def add_seconds(self, second):
        return self.add(seconds=second)

    def sub_seconds(self, second):
        return self.sub(seconds=second)

    '''recent value'''
    def approach(self, other, offset=1):
        return abs(self.time_stamp_microsecond - self.__class__(other).time_stamp_microsecond) <= offset * 1000

    def __lt__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __le__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __gt__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __ge__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __eq__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __ne__(self, other):
        return self.time_stamp_microsecond < self.__class__(other).time_stamp_microsecond

    def __str__(self):
        return str(self._datetime)