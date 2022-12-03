"""
Executes the provided function once for each list element, starting from
the list's last element.
"""


def fn_for_each_in_reverse(obj: list, fn):
    for item in obj[::-1]:
        fn(item)


fn_for_each_in_reverse([1, 2, 3], print)
# >>> 3
# >>> 2
# >>> 1
