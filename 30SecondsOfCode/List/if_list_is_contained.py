"""
Checks if the elements of the first list are contained in the second one
regardless of order.
"""


def is_contained(sub_obj: list, obj: list):
    for item in set(sub_obj):
        if sub_obj.count(item) > obj.count(item):
            return False
    return True


print(is_contained([1, 4], [2, 4, 1]))
# >>> True
