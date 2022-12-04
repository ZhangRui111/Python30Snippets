"""
Returns a list with n elements removed from the right.
"""


def drop_from_right(obj: list, n=1):
    return obj[:-n]


print(drop_from_right([1, 2, 3]))
# >>> [1, 2]
print(drop_from_right([1, 2, 3], 2))
# >>> [1]
print(drop_from_right([1, 2, 3], 42))
# >>> []
