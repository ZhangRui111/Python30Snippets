"""
Pads a string on both sides with the specified character, if it's shorter
than the specified length.
"""
from math import floor


def pad(s, length, char=' '):
    return s.rjust(floor((len(s) + length) / 2), char).ljust(length, char)


pad('cat', 8)  # '  cat   '
pad('42', 6, '0')  # '004200'
pad('foobar', 3)  # 'foobar'

# -------------------- more --------------------
# 1. str.rjust(), str.ljust() and str.center()
#   The str.rjust() method returns a new string of given length after
#   substituting a given character in left side of original string, i.e.,
#   right align the string with left-padding.
#   The str.ljust() method returns a new string of given length after
#   substituting a given character in right side of original string, i.e.,
#   left align the string with right-padding.
#   The str.center() method center aligns the string, using a specified
#   character (space is default) as the fill character.
print("hello".rjust(8, '+'))
print("hello".ljust(8, '+'))
print("hello".center(8, '+'))
# >>> +++hello
# >>> hello+++
# >>> +hello++
#
# 2. Python zfill & rjust
# Refer to String/pad_number.py
