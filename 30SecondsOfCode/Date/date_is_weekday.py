"""
Checks if the given date is a weekday.
"""
from datetime import date


def date_is_weekday(d: date = date.today()):
    # return False if d.weekday() > 4 else True
    return d.weekday() < 5


print(date_is_weekday())
print(date_is_weekday(date(2022, 11, 26)))
print(date_is_weekday(date(2022, 12, 2)))

# -------------------- more --------------------
# 1. date.weekday(): Return day of the week, where
# Monday == 0 ... Sunday == 6.
# 2. datetime.weekday(): datetime is the sub-class of date,
