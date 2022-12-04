"""
Counts the occurrences of a value in a list.
"""


def count_occurrences(obj: list, val):
    return obj.count(val)


print(count_occurrences([1, 1, 2, 1, 2, 3], 1))
# >>> 3
