"""
Calculates the Hamming distance between two values.
"""


def hamming_distance(a, b):
    return bin(a ^ b).count('1')


print(hamming_distance(2, 3))
# >>> 1

# -------------------- more --------------------
print("-" * 40)

# 1. The Hamming distance between two integers is the number of positions
#    at which the corresponding bits are different.
#
# 2. count()
#    Syntax: S.count(sub[, start[, end]]) -> int
#
#    Return the number of non-overlapping occurrences of substring sub in
#    string S[start:end].
print("ssss".count('ss'))
# >> 2
#
# 3. bin()
#    Return the binary representation of an integer.
print(bin(8))
# 3. Python Bitwise Operators
# OPERATOR	     DESCRIPTION	   SYNTAX
#    &	         Bitwise AND	   x & y
#    |	         Bitwise OR	       x | y
#    ~	         Bitwise NOT	     ~x
#    ^	         Bitwise XOR	   x ^ y
#    >>	    Bitwise right shift	    x>>
#    <<	    Bitwise left shift	    x<<
print()
print("& | ~ ^")
a = int(10)
b = int(6)
print(a, "{:08b}".format(a))
print(b, "{:08b}".format(b))
print(a & b, "{:08b}".format(a & b))
print(a | b, "{:08b}".format(a | b))
print(~a, "{:08b}".format(~a))
print(a ^ b, "{:08b}".format(a ^ b))

print()
print(">> <<")
a = 14
print("a", a, "{:08b}".format(a))
print("a >> 1", a >> 1, "{:08b}".format(a >> 1))
print("a << 1", a << 1, "{:08b}".format(a << 1))

# more about ~a:
# Python uses so-called complementary binaries to represent negative integers.
# You write a negative number -x as the bit pattern for (x-1) and flip all bits
# from 1 to 0 and from 0 to 1 (complement). So, ~(x) = -(x + 1)
