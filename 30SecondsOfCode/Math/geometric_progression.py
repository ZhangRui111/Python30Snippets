"""
Initializes a list containing the numbers in the specified range where start
and end are inclusive and the ratio between two terms is step.
"""
from math import floor, log


def geometric_progression_1(end, start=1, step=2):
    """ My solution """
    res = []
    n = start
    while n <= end:
        res.append(n)
        n *= step
    return res


def geometric_progression(end, start=1, step=2):
    return [start * step ** i for i in
            range(floor(log(end / start) / log(step)) + 1)]


print(geometric_progression_1(256))
# >>> [1, 2, 4, 8, 16, 32, 64, 128, 256]
print(geometric_progression_1(256, 3))
# >>> [3, 6, 12, 24, 48, 96, 192]
print(geometric_progression_1(256, 1, 4))
# >>> [1, 4, 16, 64, 256]
