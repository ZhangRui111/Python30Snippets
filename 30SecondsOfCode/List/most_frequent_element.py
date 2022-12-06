"""
Returns the most frequent element in a list.
"""
from collections import Counter


def most_frequent_1(obj: list):
    return Counter(obj).most_common()[0][0]


def most_frequent_2(obj: list):
    return max(set(obj), key=obj.count)


print(most_frequent_1([1, 2, 1, 2, 3, 2, 1, 4, 2]))
print(most_frequent_2([1, 2, 1, 2, 3, 2, 1, 4, 2]))
# >>> 2
