"""
Maps the values of a list to a dictionary using a function, where the
key-value pairs consist of the original value as the key and the result
of the function as the value.
"""


def map_list_to_dict(obj: list, fn):
    # return {key: value for key, value in zip(lst, list(map(fn, lst)))}
    return dict(zip(obj, list(map(fn, obj))))


res = map_list_to_dict([1, 2, 3], lambda x: x * x)
print(res)
# >>> {1: 1, 2: 4, 3: 9}
