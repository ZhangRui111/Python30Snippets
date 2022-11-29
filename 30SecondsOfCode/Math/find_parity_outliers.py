"""
Finds the items that are parity outliers in a given list.
"""
from collections import Counter


def find_parity_outliers(nums):
    target = Counter([n % 2 for n in nums]).most_common()[0][0]
    return [n for n in nums if n % 2 != target]


print(find_parity_outliers([1, 2, 3, 4, 6]))
# >>> [1, 3]
print(find_parity_outliers([1, 2, 3, 5, 6]))
# >>> [2, 6]
print(find_parity_outliers([1, 2, 3, 4, 5, 6, 8]))
# >>> [1, 3, 5]
