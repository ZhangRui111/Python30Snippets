"""
Casts the provided value as a list if it's not one.
"""


def cast_list(val):
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]


print(cast_list('foo'))
# >>> ['foo']
print(cast_list([1]))
# >>> [1]
print(cast_list(('foo', 'bar')))
# >>> ['foo', 'bar']
