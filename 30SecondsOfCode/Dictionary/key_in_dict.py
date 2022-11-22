"""
Checks if the given key exists in a dictionary.
"""


def key_in_dict(obj: dict, key):
    return key in obj.keys()


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
print(key_in_dict(d, 'three'))
print(key_in_dict(d, 'six'))
