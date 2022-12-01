"""
Finds the index of the first element in the given list that satisfies the
provided testing function.
"""


def find_first_matching_index_0(obj: list, fn):
    """ My solution """
    return list(map(fn, obj)).index(True)


def find_first_matching_index_1(obj: list, fn):
    """ My solution """
    return next(i for i, item in enumerate(obj) if fn(item))


print(find_first_matching_index_0([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 0
print(find_first_matching_index_1([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 0
