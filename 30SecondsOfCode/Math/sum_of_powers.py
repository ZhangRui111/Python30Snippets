"""
Returns the sum of the powers of all the numbers from start to end
(both inclusive).
"""


def sum_of_powers(end, power=2, start=1):
    return sum([pow(n, power) for n in range(start, end + 1)])


print(sum_of_powers(10))
# >>> 385
print(sum_of_powers(10, 3))
# >>> 3025
print(sum_of_powers(10, 3, 5))
# >>> 2925
