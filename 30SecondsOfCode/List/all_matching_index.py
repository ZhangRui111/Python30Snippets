"""
Finds the indexes of all elements in the given list that satisfy the
provided testing function.
"""


# def find_all_matching_index(obj: list, fn):
#     """
#     A wrong solution
#     filter() returns the items rather than indexes.
#     """
#     return list(filter(fn, obj))


def find_all_matching_index(obj: list, fn):
    return [i for i, item in enumerate(obj) if fn(item)]


print(find_all_matching_index([1, 2, 3, 4], lambda n: n % 2 == 1))
# >>> [0, 2]
