"""
Checks if all elements in a list are identical.
"""


def all_identical(lst):
    return len(set(lst)) == 1


print(all_identical([1, 2, 3, 4, 5, 6]))
# >>> False
print(all_identical([1, 1, 1, 1]))
# >>> True
