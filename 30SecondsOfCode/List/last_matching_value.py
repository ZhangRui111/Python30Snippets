"""
Finds the value of the last element in the given list that satisfies
the provided testing function.
"""


def find_last_matching_value_1(obj: list, fn):
    return next(filter(fn, obj[::-1]))


def find_last_matching_value_2(obj: list, fn):
    return next(x for x in obj[::-1] if fn(x))


print(find_last_matching_value_1([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 3
