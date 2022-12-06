"""
Moves the specified amount of elements to the end of the list
"""


def offset_end_1(obj: list, n: int):
    len_obj = len(obj)
    obj.extend(obj[:n])
    return obj[-len_obj:]


def offset_end_2(obj: list, n: int):
    return obj[n:] + obj[:n]


print(offset_end_1([1, 2, 3, 4, 5], 2))
# >>> [3, 4, 5, 1, 2]
print(offset_end_1([1, 2, 3, 4, 5], -2))
# >>> [4, 5, 1, 2, 3]
print(offset_end_2([1, 2, 3, 4, 5], 2))
# >>> [3, 4, 5, 1, 2]
print(offset_end_2([1, 2, 3, 4, 5], -2))
# >>> [4, 5, 1, 2, 3]
