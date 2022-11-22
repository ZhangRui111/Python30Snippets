"""
Calculates the month difference between two dates.
"""
from math import ceil, floor
from datetime import date


def months_diff(start: date, end: date):
    return ceil((end - start).days / 30)


start = date(2022, 10, 28)
end = date(2022, 11, 21)
print(months_diff(start, end))

# -------------------- more --------------------
# ceil() 上取整
print(ceil(5.5))
print(ceil(-5.5))
# floor() 下取整
print(floor(5.5))
print(floor(-5.5))
# int() 靠近0取整
print(int(5.5))
print(int(-5.5))
