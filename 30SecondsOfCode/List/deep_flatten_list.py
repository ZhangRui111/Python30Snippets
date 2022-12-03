"""
Deep flattens a list.
"""
from collections.abc import Iterable
from itertools import chain


def deep_flatten(obj):
    if isinstance(obj, Iterable):
        res = []
        for item in obj:
            for a in deep_flatten(item):
                res.append(a)
        return res
    else:
        return [obj]
    # return ([a for i in obj for a in
    #          deep_flatten(i)] if isinstance(obj, Iterable) else [obj])


print(deep_flatten([1, [2], [[3], 4], 5]))
# >>> [1, 2, 3, 4, 5]

# -------------------- more --------------------
# itertools.chain.from_iterable() is not applicable.
# (1) list(chain.from_iterable(obj)) --> TypeError: 'int' object is not iterable
try:
    print(list(chain.from_iterable([1, [2], [[3], 4], 5])))
except TypeError as e:
    print("TypeError {}".format(e))  # TypeError 'int' object is not iterable
# (2) chain and chain.from_iterable() cannot work in a recursion way, e.g.,

lst = [[1], [2, 3], [[4, 5], 6], [7]]
print(lst)
print(list(chain.from_iterable(lst)))
# >>> [[1], [2, 3], [[4, 5], 6], [7]]
# >>> [1, 2, 3, [4, 5], 6, 7]

print(list(chain([1, 2, 3], [4, 5, 6])))
print(list(chain([1, [2, 3]], [4, [5], 6])))
# >>> [1, 2, 3, 4, 5, 6]
# >>> [1, [2, 3], 4, [5], 6]
