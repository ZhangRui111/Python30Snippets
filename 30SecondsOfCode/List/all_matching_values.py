"""
Finds the value of the all element in the given list that satisfies
the provided testing function.
"""


def find_all_matching_value(obj: list, fn):
    return list(filter(fn, obj))


print(find_all_matching_value([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> [1, 3]
