"""
Checks if the provided integer is a prime number.
"""
from math import sqrt


def is_prime_1(num: int):
    """ My solution """
    if num <= 1:
        return False

    # when num == 2, skip the whole for part
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def is_prime_2(num: int):
    """ Suggested solution """
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False

    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


def is_prime_3(num: int):
    """ A better solution with less calculations """
    if num <= 1 or (num % 2 == 0 and num > 2):
        return False

    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


print(is_prime_3(2))
# >>> True
print(is_prime_3(11))
# >>> True
print(is_prime_3(25))
# >>> False
print(is_prime_3(94))
# >>> False
print(is_prime_3(107))
# >>> True

# -------------------- more --------------------
print('-' * 40)

# 1. all()
#    Return True if bool(x) is True for all values x in the iterable.
print(all([1, 2, 3, 4, 5]))
print(all([0, 2, 3, 4, 5]))
print(all(["", 1, True]))
# >>> True
# >>> False
# >>> False
#
# 2. any()
#    Return True if bool(x) is True for any x in the iterable.
print(any([1, 2, 3, 4, 5]))
print(any([0, 2, 3, 4, 5]))
print(any(["", 1, True]))
# >>> True
# >>> True
# >>> True
