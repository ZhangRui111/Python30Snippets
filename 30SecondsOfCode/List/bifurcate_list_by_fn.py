"""
Bifurcate list based on function.
"""


def bifurcate_by_fn_1(obj: list, fn):
    """ My solution """
    res = [[], []]
    for v, j in zip(obj, map(fn, obj)):
        res[0].append(v) if j else res[1].append(v)
    return res


def bifurcate_by_fn_2(obj: list, fn):
    return [
        [x for x in obj if fn(x)],
        [x for x in obj if not fn(x)],
    ]


print(bifurcate_by_fn_1(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b'))
print(bifurcate_by_fn_2(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b'))
# >>> [['beep', 'boop', 'bar'], ['foo']]
