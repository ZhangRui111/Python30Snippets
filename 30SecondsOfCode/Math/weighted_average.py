"""
Returns the weighted average of two or more numbers.
"""


def weighted_average(obj: list, weight: list):
    return sum(n * w for n, w in zip(obj, weight)) / sum(weight)


print(weighted_average([1, 2, 3], [0.6, 0.2, 0.3]))
# >>> 1.72727
