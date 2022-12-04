"""
Returns a list of elements that exist in both lists.
"""


def list_intersection_1(obj1: list, obj2: list):
    """ My solution """
    return list(set(obj1) & set(obj2))


def list_intersection_2(obj1: list, obj2: list):
    return [item for item in obj1 if item in obj2]


print(list_intersection_1([1, 2, 3], [1, 2, 4]))
print(list_intersection_2([1, 2, 3], [1, 2, 4]))
# >>> [1, 2]
