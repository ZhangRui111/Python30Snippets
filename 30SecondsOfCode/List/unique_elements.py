"""
Returns the unique elements in a given list.
"""


def unique_elements(obj: list):
    return list(set(obj))


print(unique_elements([1, 2, 2, 3, 4, 3]))
# >>> [1, 2, 3, 4]
