"""
Trim whitespace from a string.
"""
# Whitespace characters are the space ( ), tab (\t), newline (\n), and
# carriage return characters (\r).

# str.strip() method removes whitespace characters from both the beginning
# and end of a string.
print("{!r}".format('\tHello\t'.strip()))
# str.lstrip() method removes whitespace characters from the beginning of a
# string.
print("{!r}".format('\tHello\t'.lstrip()))
# str.rstrip() method removes whitespace characters from the end of a string.
print("{!r}".format('\tHello\t'.rstrip()))
