"""
Moves the specified amount of elements to the start of the list.
"""


def offset_start(obj: list, n: int):
    return obj[-n:] + obj[:-n]


print(offset_start([1, 2, 3, 4, 5], 2))
# >>> [4, 5, 1, 2, 3]
print(offset_start([1, 2, 3, 4, 5], -2))
# >>> [3, 4, 5, 1, 2]
