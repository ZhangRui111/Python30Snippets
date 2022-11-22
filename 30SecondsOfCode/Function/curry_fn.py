"""
Curries a function.
"""
from functools import partial


def curry(fn, *args):
    return partial(fn, *args)


add = lambda x, y: x + y
add10 = curry(add, 10)
print(add10(20))  # 30


# -------------------- more --------------------
# Partial functions allow us to fix a certain number of arguments of a
# function and generate a new function.

# 1. positional args
def mod(n, m):
    return n % m


print(mod(100, 7))  # 2
mod_by_100 = partial(mod, 50)  # replace the first arg (n) with 100
print(mod_by_100(7))  # 1

# 2. keyword args
bin2dec = partial(int, base=2)  # replace the keyword arg (base)
print(bin2dec('0b10001'))  # 17
print(bin2dec('10001'))  # 17

hex2dec = partial(int, base=16)  # replace the keyword arg (base)
print(hex2dec('0x67'))  # 103
print(hex2dec('67'))  # 103

# 3. demo
# A normal function


def f(a, b, c, d, x):
    return 10000 * a + 1000 * b + 100 * c + 10 * d + x


fn1 = partial(f, 3, 1, 4, 2)  # fn has only one arg (x)
print(fn1(5))  # x = 5
fn2 = partial(f, b=2, d=6)  # fn has three args (a, c, x)
print(fn2(a=3, c=4, x=5))
