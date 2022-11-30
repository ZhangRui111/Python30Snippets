"""
Generates a list of numbers in the arithmetic progression starting with the
given positive integer and up to the specified limit.
"""


def arithmetic_progression_1(start, end, step):
    res = []
    n = start
    while n <= end:
        res.append(n)
        n += step
    return res


def arithmetic_progression_2(start, end, step):
    return list(range(start, end + 1, step))


print(arithmetic_progression_1(5, 25, 5))
# >>> [5, 10, 15, 20, 25]
print(arithmetic_progression_2(5, 25, 5))
# >>> [5, 10, 15, 20, 25]
