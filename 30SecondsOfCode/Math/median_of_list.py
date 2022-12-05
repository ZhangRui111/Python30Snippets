"""
Finds the median of a list of numbers.
"""


def median(obj: list):
    obj.sort()
    len_obj = len(obj)
    if len_obj % 2 == 0:
        return (obj[int(len_obj / 2) - 1] + obj[int(len_obj / 2)]) / 2
    else:
        return obj[int((len_obj - 1) / 2)]


print(median([1]))
# >>> 1
print(median([1, 2]))
# >>> 1.5
print(median([1, 2, 3]))
# >>> 2.0
print(median([1, 2, 3, 4]))
# >>> 2.5
