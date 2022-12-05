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
print('-' * 40)

# 1. The usage of reduce: Dictionary/get_nested_value.py
# 2. double lambda --> generate a function that returns a function, e.g.,
#    the following two demos are identical functionally.


f1 = lambda x: x + 1
f2 = lambda x, y: x + y

# demo 1
compose_fn1 = lambda f, g: lambda *args: f(g(*args))
fn1 = compose_fn1(f1, f2)


# demo 2
def compose_fn2(f, g):
    def fn(*args):
        return f(g(*args))
    return fn


fn2 = compose_fn2(f1, f2)

# result
print(fn1(1, 2))
print(fn2(1, 2))
