"""
Sorts the given dictionary by key.
"""


def sort_dict_by_key(obj: dict, reverse: bool = False):
    # return dict(sorted(obj.items(), reverse=reverse,
    #                    key=lambda item: item[0]))
    return dict(sorted(obj.items(), reverse=reverse))


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
res = sort_dict_by_key(d)
print(res)
res = sort_dict_by_key(d, reverse=True)
print(res)
