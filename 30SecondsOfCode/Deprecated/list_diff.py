"""
Calculates the difference between two iterables, without filtering
duplicate values.
"""


def list_difference_1(obj1: list, obj2: list):
    _obj1, _obj2 = set(obj1), set(obj2)
    return list(_obj1 ^ _obj2)


def list_difference_2(obj1: list, obj2: list):
    _obj2 = set(obj2)
    return [item for item in obj1 if item not in _obj2]


print(list_difference_1([1, 2, 3], [1, 2, 4]))
# >>> [3, 4]
print(list_difference_1([1, 2, 3], [1, 2, 4]))
# >>> [3]
