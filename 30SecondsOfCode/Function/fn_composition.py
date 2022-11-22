"""
Performs right-to-left function composition.

- Use functools.reduce() to perform right-to-left function composition.
- The last (rightmost) function can accept one or more arguments; the
  remaining functions must be unary.
"""
from functools import reduce


def compose(*fns):
    return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


sub2 = lambda x: x - 2
add5 = lambda x: x + 5
multiply = lambda x, y: x * y
multiply_and_add_5_and_sub_2 = compose(sub2, add5, multiply)
print(multiply_and_add_5_and_sub_2(5, 2))  # 5 * 2 + 5 - 2 --> 13

# -------------------- more --------------------
# The usage of reduce: Dictionary/get_nested_value.py
