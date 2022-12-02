"""
Finds the value of the first element in the given list that satisfies
the provided testing function.
"""


def find_first_matching_value_1(obj: list, fn):
    """ My solution """
    return next(filter(fn, obj))


def find_first_matching_value_1(obj: list, fn):
    return next(x for x in obj if fn(x))


print(find_first_matching_value_1([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 1
