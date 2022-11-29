"""
Calculates the average of a list, after mapping each element to a value
using the provided function.
"""


def average_by_fn(obj: list, fn):
    return sum(map(fn, obj)) / len(obj)


print(average_by_fn([{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}],
                    lambda x: x['n']))

# -------------------- more --------------------
# sum() returns the sum of a 'start' value (default: 0) plus an
# iterable of numbers
print(sum([1, 1, 1], 0))
# >>> 3
print(sum([1, 1, 1], 3))
# >>> 6
