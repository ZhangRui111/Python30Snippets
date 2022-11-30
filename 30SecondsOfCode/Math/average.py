"""
Calculates the average of two or more numbers.
"""


def average(*args):
    return sum(args) / len(args)


print(average(*[1, 2, 3, 4]))
# >>> 2.5
print(average(1, 2, 3))
# >>> 2.0
