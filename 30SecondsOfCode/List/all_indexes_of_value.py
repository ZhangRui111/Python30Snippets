"""
Returns a list of indexes of all the occurrences of an element in a list.
"""


def index_of_all(obj: list, value):
    return [i for i, x in enumerate(obj) if x == value]


print(index_of_all([1, 2, 1, 4, 5, 1], 1))
# >>> [0, 2, 5]
print(index_of_all([1, 2, 3, 4], 6))
# >>> []
