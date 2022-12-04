"""
Checks if two lists contain the same elements regardless of order.
"""
from collections import Counter


def have_same_contents_1(obj1: list, obj2: list):
    """ My solution """
    return sorted(obj1) == sorted(obj2)


def have_same_contents_2(obj1: list, obj2: list):
    """ My solution 2 """
    return Counter(obj1) == Counter(obj2)


def have_same_contents_3(obj1: list, obj2: list):
    for v in set(obj1 + obj2):
        if obj1.count(v) != obj2.count(v):
            return False
    return True


print(have_same_contents_1([1, 2, 4], [2, 4, 1]))
print(have_same_contents_1([1, 2, 4], [2, 4, 0]))
print(have_same_contents_2([1, 2, 4], [2, 4, 1]))
print(have_same_contents_2([1, 2, 4], [2, 4, 0]))
print(have_same_contents_3([1, 2, 4], [2, 4, 1]))
print(have_same_contents_3([1, 2, 4], [2, 4, 0]))
# >>> True
# >>> False
