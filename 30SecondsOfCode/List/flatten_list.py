"""
Flattens a list, by spreading its elements into a new list.
"""


def flatten(obj: list):
    res = []
    for item in obj:
        res.append(item) if isinstance(item, int) else res.extend(item)
    return res


print(flatten([1, 2, 3, [4, 5, 6], [7], 8, 9]))
# >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# -------------------- more --------------------
# Refer to List/deep_flatten_list.py
