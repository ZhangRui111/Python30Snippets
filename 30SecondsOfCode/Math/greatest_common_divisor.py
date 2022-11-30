"""
Calculates the greatest common divisor of a list of numbers.
"""
from functools import reduce
from math import gcd


def greatest_common_divisor_1(obj: list):
    """ BF """
    min_n = min(obj)
    res = 1
    for i in range(2, min_n):
        for n in obj:
            if n % i != 0:
                break
            res = max(res, i)
    return res


def greatest_common_divisor_2(obj: list):
    return reduce(gcd, obj)


print(greatest_common_divisor_2([8, 36, 28]))
# >>> 4
