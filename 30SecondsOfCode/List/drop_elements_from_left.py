"""
Returns a list with n elements removed from the right.
"""


def drop_from_left(obj: list, n=1):
    return obj[n:]


print(drop_from_left([1, 2, 3]))
# >>> [2, 3]
print(drop_from_left([1, 2, 3], 2))
# >>> [3]
print(drop_from_left([1, 2, 3], 42))
# >>> []
