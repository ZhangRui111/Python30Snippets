"""
Checks if all the values in a list are unique.
"""
from collections import Counter


def all_unique_1(obj: list):
    return len(set(obj)) == len(obj)


def all_unique_2(obj: list):
    return Counter(obj).most_common()[0][1] == 1


print(all_unique_1([1, 2, 3, 4, 5, 6]))
print(all_unique_1([1, 2, 2, 3, 4, 5]))
print(all_unique_2([1, 2, 3, 4, 5, 6]))
print(all_unique_2([1, 2, 2, 3, 4, 5]))
# >>> True
# >>> False
