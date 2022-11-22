"""
Tests a value, x, against a testing function, conditionally applying a function.
"""


def when(condition_fn, when_true_fn):
    return lambda x: when_true_fn(x) if condition_fn(x) else x


double_even_numbers = when(lambda x: x % 2 == 0, lambda x: x * 2)
print(double_even_numbers(2))  # 4
print(double_even_numbers(1))  # 1
