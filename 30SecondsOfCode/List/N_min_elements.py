"""
Returns the n minimum elements from the provided list.
"""


def min_n(obj: list, n: int = 1):
    return sorted(obj, reverse=False)[:n]


print(min_n([1, 2, 3]))
# >>> [1]
print(min_n([1, 2, 3], 2))
# >>> [1, 2]
