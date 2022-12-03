"""
Checks if the provided function returns True for at least one element in
the list.
"""


def any_is_true(obj: list, fn=lambda x: x):
    return any(map(fn, obj))


print(any_is_true([4, 2, 3], lambda x: x > 5))
# >>> False
print(any_is_true([1, 2, 3]))
# >>> True
print(any_is_true([4, 1, 3], lambda x: x % 2 == 0))
# >>> True
print(any_is_true([0, 2, 0]))
# >>> True
