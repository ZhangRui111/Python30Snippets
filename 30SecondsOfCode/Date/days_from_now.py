"""
Calculates the date of n days from today.
"""
from datetime import timedelta, date


def days_from_now(n: int):
    return date.today() + timedelta(n)


print(days_from_now(2))
