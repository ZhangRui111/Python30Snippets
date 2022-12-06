"""
Reverses a number.
"""
from math import copysign


def reverse_number_1(num):
    neg = True if num < 0 else False
    num = abs(num)

    rev_num = str(num)[::-1]

    # rev_num = [c for c in str(num)]
    # rev_num.reverse()
    # rev_num = "".join(rev_num)

    return -float(rev_num) if neg else float(rev_num)


def reverse_number_2(n):
    return copysign(float(str(n)[::-1].replace('-', '')), n)


print(reverse_number_1(981))
# >>> 189
print(reverse_number_1(-500))
# >>> -5
print(reverse_number_1(73.6))
# >>> 6.37
print(reverse_number_1(-5.23))
# >>> -32.5

# -------------------- more --------------------
print(copysign(5, -9))
print(copysign(5, -6))
print(copysign(5, 6))
# >>> -5.0
# >>> -5.0
# >>> 5.0
