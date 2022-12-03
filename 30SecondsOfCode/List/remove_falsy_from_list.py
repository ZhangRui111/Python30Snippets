"""
Removes falsy values (False, None, 0, and "") from a list.
"""


def compact_list_1(obj: list):
    """ My solution """
    return [item for item in obj if item]


def compact_list_2(obj: list):
    return list(filter(None, obj))


print(compact_list_1([0, 1, False, 2, '', 3, 'a', 's', 34]))
print(compact_list_2([0, 1, False, 2, '', 3, 'a', 's', 34]))
# >>> [ 1, 2, 3, 'a', 's', 34 ]

# -------------------- more --------------------
# filter(function or None, iterable) --> filter object
#   Return an iterator yielding those items of iterable for which
#   function(item) is true.
#   If function is None, return the items that are true.
