"""
Finds the index of the last element in the given list that satisfies the
provided testing function.
"""


def find_last_matching_index_0(obj: list, fn):
    """ My solution """
    return len(obj) - 1 - list(map(fn, reversed(obj))).index(True)


def find_last_matching_index_1(obj: list, fn):
    return len(obj) - 1 - next(i for i, item in
                               enumerate(obj[::-1]) if fn(item))


print(find_last_matching_index_0([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 2
print(find_last_matching_index_1([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> 2
