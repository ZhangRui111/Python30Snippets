"""
Reverses a list or a string.
"""


def reverse(itr):
    return itr[::-1]


print(reverse([1, 2, 3]))
# >>> [3, 2, 1]
print(reverse('snippet'))
# >>> 'teppins'
