"""
Returns all the elements of a list except the last one
"""


def list_without_last_element(obj: list):
    return obj[:-1]


print(list_without_last_element([1, 2, 3]))
# >>> [1, 2]
