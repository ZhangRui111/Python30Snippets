"""
Calculates the date of n days ago from today.
"""
from datetime import timedelta, date


def days_ago(n: int):
    return date.today() - timedelta(n)


print(days_ago(10))
