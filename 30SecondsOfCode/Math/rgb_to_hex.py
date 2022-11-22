def rgb_to_hex(r, g, b):
    return ("{:02X}" * 3).format(r, g, b)


print(rgb_to_hex(255, 165, 1))  # 'FFA501'

# -------------------- more --------------------
# str.format()
# 1. zero-padded: "{:0[length][type]}".format()
# 2. data type
# Type	Meaning
#  d	Decimal integer [10]
#  b	Binary format [2]
#  o	Octal format [8]
#  x	Hexadecimal format [16] (lower case)
#  X	Hexadecimal format [16] (upper case)
#  n	Same as 'd'. Except it uses current locale setting for number separator
#  e	Exponential notation. (lowercase e)
#  E	Exponential notation (uppercase E)
#  f	Displays fixed point number (Default: 6)
#  F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
#  g	General format. Rounds number to p significant digits.
#       (Default precision: 6)
#  G	Same as 'g'. Except switches to 'E' if the number is large.
#  c	Corresponding Unicode character
#  %	Percentage. Multiples by 100 and puts % at the end.

print('-' * 40)
#  d	Decimal integer [10]
print("Decimal integer [10]: {:d}".format(127))
#  b	Binary format [2]
print("Binary format [2]: {:b}".format(127))
print("Binary format (zero padding) [2]: {:08b}".format(127))
#  o	Octal format [8]
print("Octal format [8]: {:o}".format(127))
#  x	Hexadecimal format [16] (lower case)
print("Hexadecimal format [16] (lower case): {:x}".format(127))
#  X	Hexadecimal format [16] (upper case)
print("Hexadecimal format [16] (upper case): {:X}".format(127))
#  n	Same as 'd'. Except it uses current locale setting for number separator
print("Decimal integer [10] (locale setting for number separator): {:n}".
      format(127985000))
#  e	Exponential notation. (lowercase e)
print("Exponential notation. (lowercase e): {:e}".format(127))
#  E	Exponential notation (uppercase E)
print("Exponential notation (uppercase E): {:E}".format(127))
#  f	Displays fixed point number (Default: 6)
print("Float: {:f}".format(127.45))
#  F	Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
print("Float: {:F}".format(127.45))
#  g	General format. Rounds number to p significant digits.
#       (Default precision: 6)
print("General format: {:g}".format(127))
print("General format: {:g}".format(127.45))
print("General format: {:g}".format(12700000000))
#  G	Same as 'g'. Except switches to 'E' if the number is large.
print("General format: {:G}".format(127))
print("General format: {:G}".format(127.45))
print("General format: {:G}".format(12700000000))
#  c	Corresponding Unicode character
print("Corresponding Unicode character {:c} of {:d}".format(100, 100))
#  %	Percentage. Multiples by 100 and puts % at the end.
print("Percentage: {:%}".format(0.45))
