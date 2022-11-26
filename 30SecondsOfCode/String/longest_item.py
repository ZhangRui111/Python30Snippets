"""
Takes any number of iterable objects or objects with a length property
and returns the longest one.
"""


def longest_item(*args):
    return max(args, key=len)


print(longest_item('this', 'is', 'a', 'testcase'))
# >>> 'testcase'
print(longest_item([1, 2, 3], [1, 2], [1, 2, 3, 4, 5]))
# >>> [1, 2, 3, 4, 5]
print(longest_item([1, 2, 3], 'foobar'))
# >>> 'foobar'
