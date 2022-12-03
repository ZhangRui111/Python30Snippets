"""
Returns the symmetric difference between two iterables, without filtering
out duplicate values.
"""


def symmetric_difference(a, b):
    (_a, _b) = (set(a), set(b))
    return [item for item in a if item not in _b] + [item for item in b
                                                     if item not in _a]


print(symmetric_difference([1, 2, 3], [1, 2, 4]))
# >>> [3, 4]
