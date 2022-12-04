"""
Checks if any element in values are included in the list.
"""


def includes_any(obj: list, values: list):
    for v in values:
        if v in obj:
            return True
    return False


print(includes_any([1, 2, 3, 4], [2, 9]))
# >>> True
print(includes_any([1, 2, 3, 4], [8, 9]))
# >>> False
