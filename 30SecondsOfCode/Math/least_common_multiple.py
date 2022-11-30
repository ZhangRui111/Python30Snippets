"""
Calculates the least common multiple of a list of numbers.
"""
from functools import reduce
from math import gcd


def least_common_multiple(obj: list):
    return reduce(lambda x, y: int((x * y) / gcd(x, y)), obj)


print(least_common_multiple([12, 7]))
# >>> 84
print(least_common_multiple([1, 3, 4, 5]))
# >>> 60

# -------------------- more --------------------
# The least common multiple (x, y)
#     = (x * y) / the greatest common divisor (x, y)
