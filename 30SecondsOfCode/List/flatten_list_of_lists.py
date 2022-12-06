"""
Flattens a list of lists once.
"""
from itertools import chain


def flatten_1(obj: list):
    return list(chain.from_iterable(obj))


def flatten_2(obj: list):
    return [i for item in obj for i in item]


print(flatten_1([[1, 2, 3, 4], [5, 6, 7, 8]]))
print(flatten_2([[1, 2, 3, 4], [5, 6, 7, 8]]))
# >>> [1, 2, 3, 4, 5, 6, 7, 8]
