"""
Converts a number to a list of digits.
"""
from timeit import Timer


def digitize_1(n):
    return list(map(int, str(n)))


def digitize_2(n):
    return [int(c) for c in str(n)]


print(digitize_1(123))  # [1, 2, 3]
print(digitize_2(123))  # [1, 2, 3]

# -------------------- more --------------------
print('-' * 40)

# map() function returns a map object(which is an iterator) of the
# results after applying the given function to each item of a given
# iterable (list, tuple etc.)
# Syntax :
#     map(fun, iter)
# NOTE : You can pass one or multiple iterables to the map() function.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

# map vs. list comprehension
print(Timer('list(map(int, str(n)))', 'n = 123').timeit())
print(Timer('[int(c) for c in str(n)]', 'n = 123').timeit())
print(Timer('list(map(int, str(n)))', 'n = 123456').timeit())
print(Timer('[int(c) for c in str(n)]', 'n = 123456').timeit())
