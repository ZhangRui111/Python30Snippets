"""
Combines two or more dictionaries, creating a list of values for each key.
"""
from collections import defaultdict


def combine_values(*dicts):
    res = defaultdict(list)
    for d in dicts:
        for key in d:
            res[key].append(d[key])
    return dict(res)


d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}
d3 = {'a': 5, 'd': 'item', 'e': -1}

print(combine_values(d1, d2, d3))
# {'a': [1, 3, 5], 'b': ['foo', 200], 'c': [400], 'd': [400, 'item'], 'e': [-1]}
