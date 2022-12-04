"""
Returns every element that exists in any of the two lists once.
"""


def list_union(a, b):
    return list(set(a + b))
    # return list(set(a) | set(b))  # equally


print(list_union([1, 2, 3], [4, 3, 2]))
# >>> [1, 2, 3, 4]
