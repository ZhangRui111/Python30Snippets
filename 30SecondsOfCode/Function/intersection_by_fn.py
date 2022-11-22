"""
Returns a list of elements that exist in both lists, after applying the
provided function to each list element of both.
"""
from math import floor


def intersection_by_fn(obj1: list, obj2: list, fn):
    _obj1 = set(map(fn, obj1))
    _obj2 = set(map(fn, obj2))
    return [item for item in obj1 if fn(item) in _obj2], \
           [item for item in obj2 if fn(item) in _obj1]


a, b = intersection_by_fn([2.1, 1.2], [2.3, 3.4], floor)
print(a, b)
a, b = intersection_by_fn([{'x': 2}, {'x': 1}], [{'x': 1}], lambda v: v['x'])
print(a, b)
a, b = intersection_by_fn([{'x': 1}], [{'x': 2}, {'x': 1}], lambda v: v['x'])
print(a, b)
# >>> [2.1] [2.3]
# >>> [{'x': 1}] [{'x': 1}]
# >>> [{'x': 1}] [{'x': 1}]
