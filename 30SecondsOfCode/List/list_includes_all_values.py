"""
Checks if all the elements in values are included in the list.
"""


def includes_all(obj: list, values: list):
    for v in values:
        if v not in obj:
            return False
    return True


print(includes_all([1, 2, 3, 4], [1, 1, 4]))
# >>> True
print(includes_all([1, 2, 3, 4], [1, 4]))
# >>> True
print(includes_all([1, 2, 3, 4], [1, 5]))
# >>> False
