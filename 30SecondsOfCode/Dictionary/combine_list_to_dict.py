"""
Combines two lists into a dictionary, where the elements of the first one
serve as the keys and the elements of the second one serve as the values.
The values of the first list need to be unique and hashable.
"""


def list_to_dictionary(obj1: list, obj2: list):
    # return {k: v for k, v in zip(obj1, obj2)}
    return dict(zip(obj1, obj2))


res = list_to_dictionary(['a', 'b'], [1, 2])
print(res)
# >>> {a: 1, b: 2}
