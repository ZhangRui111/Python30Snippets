"""
Code Anatomy - Writing high performance Python code
"""
from timeit import Timer


def difference_1(a, b):
    return [item for item in a if item not in b]
# doesn't account for duplicates in b.


def difference_2(a, b):
    return [item for item in a if item not in set(b)]
# set() is called for every item in a.


def difference_3(a, b):
    _b = set(b)
    return [item for item in a if item not in _b]
# better one
# difference_3() uses list comprehension


def difference_4(a, b):
    _b = set(b)
    return list(filter(lambda item: item not in _b, a))
# worse than difference_3() that uses list comprehension.
# Using list comprehension can be up to ten times faster than the alternative.
# This is due to list comprehension being a native language feature that works
# very similar to a simple for loop without the overhead of the extra function
# calls.


def _difference_1():
    a = [0, 1, 2, 3, 4, 5]
    b = [0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4,
         6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10]
    return [item for item in a if item not in b]


def _difference_2():
    a = [0, 1, 2, 3, 4, 5]
    b = [0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4,
         6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10]
    return [item for item in a if item not in set(b)]


def _difference_3():
    a = [0, 1, 2, 3, 4, 5]
    b = [0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4,
         6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10]
    _b = set(b)
    return [item for item in a if item not in _b]


def _difference_4():
    a = [0, 1, 2, 3, 4, 5]
    b = [0, 0, 0, 0, 2, 2, 2, 2, 4, 4, 4, 4,
         6, 6, 6, 6, 8, 8, 8, 8, 10, 10, 10, 10]
    _b = set(b)
    return list(filter(lambda item: item not in _b, a))


def main():
    t1 = Timer('_difference_1()', 'from __main__ import _difference_1').timeit()
    t2 = Timer('_difference_2()', 'from __main__ import _difference_2').timeit()
    t3 = Timer('_difference_3()', 'from __main__ import _difference_3').timeit()
    t4 = Timer('_difference_4()', 'from __main__ import _difference_4').timeit()
    print(t1)
    print(t2)
    print(t3)
    print(t4)


if __name__ == '__main__':
    main()


# -------------------- more --------------------
# The filter() function extracts elements from an iterable (list, tuple etc.)
# for which the function returns True.
# Syntax: filter(function, iterable)
#
# # demo
# nums = [0, 1, 2, 3, 4, 5, 6, 7]
# even_nums_iterator = filter(lambda item: item % 2 == 0, nums)
# even_nums = list(even_nums_iterator)
# print(even_nums)
# # >>> [0, 2, 4, 6]
#
# If function is None, return the items that are true.
#
# # demo
# random_list = [1, 'a', 0, False, True, '0']
# filtered_iterator = filter(None, random_list)
# filtered_list = list(filtered_iterator)
# print(filtered_list)
# # >>> [1, 'a', True, '0']
