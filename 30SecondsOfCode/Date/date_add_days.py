"""
Calculates the date of n days from the given date.
"""
from datetime import date, timedelta


def date_add_days(start: date, n: int):
    return start + timedelta(n)


print(date_add_days(date.today(), 10))
print(date_add_days(date(2022, 10, 1), 10))
print(date_add_days(date(2022, 10, 1), -10))
