"""
Calculates the sum of a list, after mapping each element to a value using
the provided function.
"""


def sum_by_fn(lst, fn):
    return sum(map(fn, lst))


print(sum_by_fn([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}], lambda v: v['n']))
# >>> 20
