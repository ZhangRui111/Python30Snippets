"""
Creates a list of dates between start (inclusive) and end (not inclusive).
"""
from datetime import timedelta, date, datetime


def date_range(start: date, end: date):
    return [start + timedelta(n) for n in range(int((end - start).days))]


def _date_range(start: date, end: date):
    res = []
    alpha = end - start  # <type: timedelta>
    max_n = (end - start).days
    for n in range(int(max_n)):
        alpha = timedelta(n)  # <type: timedelta>
        day = start + timedelta(n)  # <type: date>
        print("New day: {}".format(day))
        res.append(day)
    return res


start = date(2020, 10, 1)  # <type: date>
end = date(2020, 10, 5)  # <type: date>
print("start: {}".format(start))
print("end: {}".format(end))
# _date_range(start, end)
print(date_range(start, end))

# -------------------- more --------------------
# 1. apply date/datetime + timedelta for date calculator
start = date(2016, 11, 7)
end = start + timedelta(1000)
print("1000-days anniversary: {}".format(end))

start = datetime(2016, 11, 7, 23, 30, 0)
end = start + timedelta(1000)
print("1000-days anniversary: {}".format(end))

# 2. datetime is a sub-class of date
