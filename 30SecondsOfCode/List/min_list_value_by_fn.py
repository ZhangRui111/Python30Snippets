"""
Returns the minimum value of a list, after mapping each element to a value
using the provided function.
"""


def min_by_fn(lst, fn):
    return min(map(fn, lst))


print(min_by_fn([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']))
# >>> 2
