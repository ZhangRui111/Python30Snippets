"""
Returns the maximum value of a list, after mapping each element to a value
using the provided function.
"""


def max_by_fn(lst, fn):
    return max(map(fn, lst))


print(max_by_fn([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']))
# >>> 8
