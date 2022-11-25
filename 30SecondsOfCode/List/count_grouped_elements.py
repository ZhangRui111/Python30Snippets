"""
Groups the elements of a list based on the given function and returns the
count of elements in each group.
"""
from math import floor
from collections import defaultdict


def count_by_fn(obj: list, fn):
    count = defaultdict(int)
    for v in map(fn, obj):
        count[v] += 1
    return dict(count)


res = count_by_fn([6.1, 4.2, 6.3], floor)
print(res)
# >>> {6: 2, 4: 1}
res = count_by_fn(['one', 'two', 'three'], len)
print(res)
# >>> {3: 2, 5: 1}

# -------------------- more --------------------
print('-' * 40)

# 1. defaultdict with specific default value
a = defaultdict(lambda: 1)
print(a['k1'])
a = defaultdict(lambda: 'hello')
print(a['k1'])
