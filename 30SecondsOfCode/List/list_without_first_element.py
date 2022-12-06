"""
Returns all elements in a list except for the first one.
"""


def list_without_first_element(obj: list):
    return obj[1:]


print(list_without_first_element([1, 2, 3]))
# >>> [2, 3]
print(list_without_first_element([1]))
# >>> []
