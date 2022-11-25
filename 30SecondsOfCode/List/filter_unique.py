"""
Filter unique list values
"""
from collections import Counter


def filter_non_unique_1(obj: list):
    """ My solution """
    _obj = set(obj)
    return [i for i in _obj if obj.count(i) != 1]


def filter_non_unique_2(obj: list):
    return [item for item, count in Counter(obj).items() if count != 1]


print(filter_non_unique_2([1, 2, 2, 3, 4, 4, 5]))
# >>> [2, 4]

# -------------------- more --------------------
# Refer to List/filter_non_unique.py
