import datetime
from functools import wraps


def seconds_to_duration_text(duration_in_sec):
    if duration_in_sec < 60:
        txt = f"0:{str(duration_in_sec).zfill(2)}"
        return txt

    if duration_in_sec < 60 * 60:
        mins = int(duration_in_sec / 60)
        sec = duration_in_sec % 60
        txt = f"{str(mins).zfill(2)}:{str(sec).zfill(2)}"
        if mins > 0:
            txt = txt.lstrip('0')
        return txt

    hrs = int(duration_in_sec / 60 / 60)
    mins = int(duration_in_sec / 60)
    sec = duration_in_sec % 60
    txt = f"{hrs}:{str(mins - hrs * 60).zfill(2)}:{str(sec).zfill(2)}"
    if hrs > 0:
        txt = txt.lstrip('0')
    return txt


def month_name_from_date(date) -> str:
    months = {
        1: "Jan",
        2: "Feb",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "Aug",
        9: "Sept",
        10: "Oct",
        11: "Nov",
        12: "Dec",
    }
    return months[date.month]


def date_suffix(date: datetime.datetime) -> str:
    day = date.day % 10
    if day == 1:
        return "st"
    elif day == 2:
        return "nd"
    elif day == 3:
        return "rd"
    else:
        return "th"  # noqa: FURB126


class timed_block:
    def __init__(self, message: str):
        self.message = message
        self.t0 = None
        self.dt = None

    def __enter__(self):
        self.t0 = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dt = datetime.datetime.now() - self.t0
        print(f'{self.message}. Complete in {self.dt.total_seconds() * 1000:,} ms.')


def timed(method):
    @wraps(method)
    def timed_method(*args, **kw):
        t0 = datetime.datetime.now()
        result = method(*args, **kw)
        t1 = datetime.datetime.now()

        dt = t1 - t0
        print(f"  *** timings: {method.__name__} ran in {dt.total_seconds() * 1000:,.3f} ms")

        return result

    return timed_method


def timed_async(method):
    async def timed_method(*args, **kw):
        t0 = datetime.datetime.now()
        result = await method(*args, **kw)
        t1 = datetime.datetime.now()

        dt = t1 - t0
        print(f"  *** timings: {method.__name__} ran in {dt.total_seconds() * 1000:,.3f} ms")

        return result

    return timed_method
