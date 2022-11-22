"""
Finds the key of the maximum value in a dictionary.
"""


def key_of_max_value(obj: dict):
    # return max(obj.items(), key=lambda item: item[1])[0]
    return max(obj, key=obj.get)


res = key_of_max_value({'a': 4, 'b': 0, 'c': 13})
print(res)
# >>> c
