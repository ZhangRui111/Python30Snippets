"""
Executes the provided function once for each list element.
"""


def fn_for_each(obj: list, fn):
    for item in obj:
        fn(item)


fn_for_each([1, 2, 3], print)
# >>> 1
# >>> 2
# >>> 3
