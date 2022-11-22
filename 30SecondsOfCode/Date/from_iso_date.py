"""
Converts a date from its ISO-8601 representation.
"""
from datetime import datetime


def from_iso_date(d: str):
    return datetime.fromisoformat(d)


dt = from_iso_date('2020-10-28T12:30:59.000000')  # <type: datetime>
print(dt)  # 2020-10-28 12:30:59

# -------------------- more --------------------
# 1. datetime.fromisoformat(d) appears since python 3.7
#
# 2.
# ISO 8601 is an internationally agreed way to represent dates.
# In Python ISO 8601 date is represented in YYYY-MM-DDTHH:MM:SS.mmmmmm format.
# For example, May 18, 2022, is represented as 2022-05-18T11:40:22.519222.
#
# Here:
# YYYY: Year in four-digit format
# MM: Months from 1-12
# DD: Days from 1 to 31
# T: It is the separator character that is to be printed between the date and
#    time fields. It is an optional parameter having a default value of “T”.
# HH: For the value of minutes
# MM: For the specified value of minutes
# SS: For the specified value of seconds
# mmmmmm: For the specified microseconds
#
# 3. datatime format and ISO format
print("-" * 40)
# Get the current datetime
date_now = datetime.now()
print("Today Datetime: {}".format(date_now))
# datetime to ISO format in string format
iso_date_now = date_now.isoformat()
print("ISO DateTime: {}".format(iso_date_now))
# get datetime from ISO format
r_date_now = datetime.fromisoformat(iso_date_now)
print("Today Datetime: {}".format(r_date_now))
