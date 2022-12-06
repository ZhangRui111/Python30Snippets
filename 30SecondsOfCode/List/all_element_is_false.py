"""
Checks if the provided function returns False for every element in the list.
"""


def all_is_false_1(obj: list, fn=lambda x: x):
    return not list(filter(None, map(fn, obj)))


def all_is_false_2(obj: list, fn=lambda x: x):
    return all([not fn(item) for item in obj])


print(all_is_false_1([0, 1, 2, 0], lambda x: x >= 2))
print(all_is_false_1([0, 0, 0]))
print(all_is_false_2([0, 1, 2, 0], lambda x: x >= 2))
print(all_is_false_2([0, 0, 0]))
# >>> False
# >>> True
