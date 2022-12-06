"""
Merges two or more lists into a list of lists, combining elements from each
of the input lists based on their positions.
"""


def merge_lists_1(*objs: list, fill_value=None):
    max_len = max(map(len, objs))
    for o in objs:
        o += [fill_value] * (max_len - len(o))
    return list(map(list, zip(*objs)))


def merge_lists_2(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            obj[i] if i < len(obj) else fill_value for obj in args
        ])
        # items = []
        # for obj in args:
        #     if i < len(obj):
        #         items.append(obj[i])
        #     else:
        #         items.append(fill_value)
        # result.append(items)
    return result


res = merge_lists_1(['a', 'b'], [1, 2], [True, False])
print(res)
# >>> [['a', 1, True], ['b', 2, False]]
res = merge_lists_1(['a'], [1, 2], [True, False])
print(res)
# >>> [['a', 1, True], [None, 2, False]]
res = merge_lists_1(['a'], [1, 2], [True, False], fill_value='_')
print(res)
# >>> [['a', 1, True], ['_', 2, False]]

# -------------------- more --------------------
print('-' * 40)

# [if-else-for] in one line of the comprehension: for > if > else
res = []
for i in [0, 1, 2, 3, 4, 5]:
    if i % 2 == 0:
        res.append((i, True))
    else:
        res.append((i, False))
print(res)

res = [(i, True) if i % 2 == 0 else (i, False) for i in [0, 1, 2, 3, 4, 5]]
print(res)

# [for-if] in one line of the comprehension: for > if
res = []
for i in [0, 1, 2, 3, 4, 5]:
    if i % 2 == 0:
        res.append((i, True))
print(res)

res = [(i, True) for i in [0, 1, 2, 3, 4, 5] if i % 2 == 0]
print(res)
