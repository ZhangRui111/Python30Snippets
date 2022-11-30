"""
Returns the binary representation of the given number.
"""


def to_binary(n):
    return bin(n)


print(to_binary(100))
# >>> 0b1100100

# -------------------- more --------------------
print('-' * 40)

# bin(): decimal to binary (10 --> 2), 0b...
print(bin(100))
# oct(): decimal to Octal (10 --> 8), 0o...
print(oct(100))
# hex(): decimal to hexadecimal (10 --> 16), 0x...
print(hex(100))
