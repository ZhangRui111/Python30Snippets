"""
Converts a dictionary to a list of tuples.
"""


def dict_to_list(obj: dict):
    # return [(k, v) for k, v in obj.items()]
    return list(obj.items())


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
res = dict_to_list(d)
print(res)
# >>> [('one', 1), ('three', 3), ('five', 5), ('two', 2), ('four', 4)]
