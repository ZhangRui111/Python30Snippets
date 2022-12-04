"""
Checks if the provided function returns True for every element in the list.
"""


def all_is_true(obj: list, fn=lambda x: x):
    return all(map(fn, obj))


print(all_is_true([4, 2, 3], lambda x: x > 1))
# >>> True
print(all_is_true([1, 2, 3]))
# >>> True
print(all_is_true([4, 2, 3], lambda x: x % 2 == 0))
# >>> False
print(all_is_true([0, 2, 3]))
# >>> False
