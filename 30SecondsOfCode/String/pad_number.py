"""
Pads a given number to the specified length.
"""


def pad_number(n, l):
    return str(n).zfill(l)


print(pad_number(1234, 6))
# >>> '001234'
print(pad_number(1234.55, 8))
# >>> '01234.55'

# -------------------- more --------------------
print('-' * 40)

# str.zfill() and str.rjust() and String Formatting
#   - The Python zfill method returns a copy of the string left filled with the
#     '0' character to make a character the length of a given width.
#   - The str.rjust() method returns a new string of given length after
#     substituting a given character in left side of original string, i.e.,
#     right align the string with left-padding.
#   - "{:0>10}".format(str)
#     - :0 to ask Python to use 0s to pad our string
#     - the >10 to indicate to pad from the left for a width of ten.
print("Left-padding:")
print("a1b2c3".zfill(8))
print("a1b2c3".rjust(8))
print("a1b2c3".rjust(8, '0'))
print("a1b2c3".rjust(8, '+'))
print("{: >8}".format("a1b2c3"))
print("{:0>8}".format("a1b2c3"))
print("{:+>8}".format("a1b2c3"))

print("Right-padding:")
print("a1b2c3".ljust(8))
print("a1b2c3".ljust(8, '0'))
print("a1b2c3".ljust(8, '+'))
print("{: <8}".format("a1b2c3"))
print("{:0<8}".format("a1b2c3"))
print("{:+<8}".format("a1b2c3"))
