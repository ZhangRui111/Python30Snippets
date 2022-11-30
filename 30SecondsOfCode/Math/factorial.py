"""
Calculates the factorial of a number.
"""
from functools import reduce
from operator import mul


def factorial_1(num: int):
    """ My solution: reduce """
    if not ((num >= 0) and isinstance(num, int)):
        raise Exception("Number can't be floating point or negative.")

    return 1 if num == 0 else reduce(mul, range(1, num + 1))


def factorial_2(num):
    """ recursion """
    if not ((num >= 0) and isinstance(num, int)):
        raise Exception("Number can't be floating point or negative.")

    return 1 if num == 0 else num * factorial_2(num - 1)


print(factorial_1(0))
# >>> 1
print(factorial_1(1))
# >>> 1
print(factorial_1(6))
# >>> 720
