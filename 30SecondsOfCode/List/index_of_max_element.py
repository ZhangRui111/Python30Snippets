"""
Returns the index of the element with the maximum value in a list.
"""


def max_element_index_1(obj: list):
    """
    Extensible to find the index of the n-th maximum element.
    i.e., sorted(zip(obj, range(len(obj))), reverse=True)[n][1]
    """
    # return sorted(zip(obj, range(len(obj))), key=lambda item: item[0])[-1][1]
    return sorted(zip(obj, range(len(obj))), reverse=True)[0][1]


def max_element_index_2(obj: list):
    return obj.index(max(obj))


print(max_element_index_1([5, 8, 9, 7, 10, 3, 0]))
# >>> 4
print(max_element_index_1([3, 5, 2, 10, 6, 7, 9]))
# >>> 3
