"""
Python's f-strings provide a more readable, concise and less error-prone way
to format strings than traditional string formatting.
"""


# 1. String interpolation
str_val = 'apples'
num_val = 42
print(f"{num_val} {str_val}")

# 2. Mathematical operations
print(f'{2 * 3}')

# 3. Printable representation, repr()
str_val = 'apples'
print(f'{str_val!r}')
print(repr(str_val))

s = "a\tb\tc\nd\te\tf"
print(s)
print(repr(s))

# 4. Number formatting
price_val = 6.12658
print(f'{price_val}')
print(f'{price_val:.2f}')

# 5. Date formatting
from datetime import datetime

date_val = datetime.utcnow()
print(date_val)
print(f'{date_val:%Y-%m-%d}')

# -------------------- more --------------------
# 1. repr() calls __repr__() of the given object.
# 2. f-string has similar functionality as the string.format()
print("-" * 40)

a = 'apple'
b = 10.156
c = "apple\tbanana"
t = datetime.utcnow()

print("f-string:")
print(f"{a} {b}")
print(f"{b * 2}")
print(f"{c!r}")
print(f"{b:6.1f}")
print(f"{t:%Y-%m-%d}")

print("-" * 40)

print("string.format():")
print("{} {}".format(a, b))
print("{}".format(b * 2))
print("{!r}".format(c))
print("{:6.1f}".format(b))
print("{:%Y-%m-%d}".format(t))
