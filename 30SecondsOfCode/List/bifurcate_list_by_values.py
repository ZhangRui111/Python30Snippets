"""
Splits values into two groups, based on the result of the given filter list.
"""


def bifurcate_by_values(obj: list, filter_lst: list):
    res = [[], []]
    for i, f in zip(obj, filter_lst):
        res[0].append(i) if f else res[1].append(i)
    return res
    # return [
    #     [x for x, flag in zip(obj, filter_lst) if flag],
    #     [x for x, flag in zip(obj, filter_lst) if not flag]
    #   ]


print(bifurcate_by_values(['beep', 'boop', 'foo', 'bar'],
                          [True, True, False, True]))
# >>> [['beep', 'boop', 'bar'], ['foo']]
