"""
Calculates the day difference between two dates.
"""
from datetime import date


def days_diff(start: date, end: date):
    return (end - start).days


start = date(2022, 10, 28)
end = date(2022, 11, 21)
print(days_diff(start, end))
