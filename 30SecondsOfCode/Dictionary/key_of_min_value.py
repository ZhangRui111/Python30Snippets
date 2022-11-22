"""
Finds the key of the minimum value in a dictionary.
"""


def key_of_min_value(obj: dict):
    # return min(obj.items(), key=lambda item: item[1])[0]
    return min(obj, key=obj.get)


res = key_of_min_value({'a': 4, 'b': 0, 'c': 13})
print(res)
# >>> b
