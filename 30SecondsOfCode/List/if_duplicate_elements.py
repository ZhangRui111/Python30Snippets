"""
Checks if there are duplicate values in a flat list.
"""


def duplicate_elements(lst):
    return len(lst) != len(set(lst))


print(duplicate_elements([1, 2, 3, 4, 5, 5]))
print(duplicate_elements([1, 2, 3, 4, 5]))
# >>> True
# >>> False
