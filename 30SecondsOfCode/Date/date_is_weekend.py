"""
Checks if the given date is a weekend.
"""
from datetime import date


def date_is_weekend(d: date = date.today()):
    return d.weekday() > 4


print(date_is_weekend())
print(date_is_weekend(date(2022, 11, 26)))
print(date_is_weekend(date(2022, 12, 2)))
