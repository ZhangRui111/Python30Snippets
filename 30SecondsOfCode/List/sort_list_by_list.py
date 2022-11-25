"""
Sorts one list based on another list containing the desired indexes.
"""
import numpy as np


def sort_by_indexes_1(lst: list, indexes: list, reverse: bool = False):
    """ My solution """
    _indexes = np.asarray(indexes).argsort().tolist()
    res = [lst[i] for i in _indexes]
    if reverse:
        res.sort(reverse=True)
    return res


def sort_by_indexes_2(lst: list, indexes: list, reverse: bool = False):
    sort_lst = sorted(zip(lst, indexes), key=lambda x: x[1], reverse=reverse)
    return [val for (val, _) in sort_lst]


a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
print(sort_by_indexes_2(a, b))
# >>> ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
print(sort_by_indexes_2(a, b, True))
# >>> ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
