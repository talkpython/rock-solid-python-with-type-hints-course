import datetime
from functools import wraps


def timed_function(func):
    @wraps(func)
    def time_it_inner(*args, **kwargs):
        t0 = datetime.datetime.now()

        try:
            return func(*args, **kwargs)
        finally:
            dt = datetime.datetime.now() - t0
            print(f"Timed function done in {dt.total_seconds() * 1000:,.1f} ms.")

    return time_it_inner
