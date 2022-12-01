"""
Groups the elements of a list based on the given function.
"""
from collections import defaultdict


def group_list_by_func(lst: list, fn):
    res = defaultdict(list)
    for item in lst:
        key = fn(item)
        res[key].append(item)
    # Use dict() to convert defaultdict to a regular dictionary
    return dict(res)


grouped_lst = group_list_by_func([-1, 1, 1, -2, 3, -3], lambda x: abs(x))
print(grouped_lst)
grouped_lst = group_list_by_func(['one', 'two', 'three'], len)
print(grouped_lst)
# >>> {1: [-1, 1, 1], 2: [-2], 3: [3, -3]}
# >>> {3: ['one', 'two'], 5: ['three']}
