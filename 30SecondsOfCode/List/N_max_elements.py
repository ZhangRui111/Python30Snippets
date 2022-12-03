"""
Returns the n maximum elements from the provided list.
"""


def max_n(obj: list, n: int = 1):
    return sorted(obj, reverse=True)[:n]


print(max_n([1, 2, 3]))
# >>> [3]
print(max_n([1, 2, 3], 2))
# >>> [3, 2]
