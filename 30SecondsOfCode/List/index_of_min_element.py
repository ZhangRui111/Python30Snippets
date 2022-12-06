"""
Returns the index of the element with the minimum value in a list.
"""


def min_element_index_1(obj: list):
    """
    Extensible to find the index of the n-th minimum element.
    i.e., sorted(zip(obj, range(len(obj))), reverse=False)[n][1]
    """
    # return sorted(zip(obj, range(len(obj))), key=lambda item: item[0])[0][1]
    return sorted(zip(obj, range(len(obj))), reverse=False)[0][1]


def min_element_index_2(obj: list):
    return obj.index(min(obj))


print(min_element_index_1([5, 8, 9, 7, 10, 3, 0]))
# >>> 6
print(min_element_index_1([3, 5, 2, 6, 10, 7, 9]))
# >>> 2
