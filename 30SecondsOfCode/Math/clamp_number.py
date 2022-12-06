"""
Clamps num within the inclusive range specified by the boundary values.
"""


def clamp_number_1(num, a, b):
    a, b = min(a, b), max(a, b)
    if a <= num <= b:
        return num

    return a if num < a else b


def clamp_number_2(num, a, b):
    a, b = min(a, b), max(a, b)
    return max(min(num, b), a)


print(clamp_number_2(2, 3, 5))
# >>> 3
print(clamp_number_2(1, -1, -5))
# >>> -1
