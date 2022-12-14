"""
Transposes a two-dimensional list.
"""


def transpose(obj: list):
    return list(zip(*obj))


print(transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
