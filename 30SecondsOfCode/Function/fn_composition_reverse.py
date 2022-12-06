"""
Performs left-to-right function composition.
"""
from functools import reduce


def compose(*fns):
    # - Use functools.reduce() to perform left-to-right function composition.
    # - The first (leftmost) function can accept one or more arguments; the
    #   remaining functions must be unary.
    return reduce(lambda f, g: lambda *args: g(f(*args)), fns)


sub2 = lambda x: x - 2
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5_and_sub_2 = compose(multiply, add5, sub2)
print(multiply_and_add_5_and_sub_2(5, 2))  # 5 * 2 + 5 - 2 --> 13
