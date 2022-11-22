"""
Sorts the given dictionary by value.
"""


def sort_dict_by_value(obj: dict, reverse: bool = False):
    return dict(sorted(obj.items(), reverse=reverse, key=lambda item: item[1]))


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
res = sort_dict_by_value(d)
print(res)
res = sort_dict_by_value(d, reverse=True)
print(res)
