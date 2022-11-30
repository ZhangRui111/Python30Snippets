"""
Checks if the given number falls within the given range.
"""


def num_in_range(n, a, b):
    return a <= n <= b if a <= b else b <= n <= a


print(num_in_range(3, 2, 5))
# >>> True
print(num_in_range(3, 4, 0))
# >>> True
print(num_in_range(2, 3, 5))
# >>> False
print(num_in_range(3, 2, 0))
# >>> False
