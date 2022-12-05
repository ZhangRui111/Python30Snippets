"""
Checks if a string is an anagram of another string (case-insensitive,
ignores spaces, punctuation and special characters).
"""
from collections import Counter


def is_anagram(s1, s2):
    return Counter(
        c.lower() for c in s1 if c.isalnum()
    ) == Counter(
        c.lower() for c in s2 if c.isalnum()
    )


print(is_anagram('#anagram', 'Nag a ram!'))
# >>> True

# -------------------- more --------------------
print('-' * 40)

# 1. str.isalnum()
# Return True if the string is an alpha-numeric string, False otherwise.
#
#   A string is alpha-numeric if all characters in the string are alpha-numeric
#   and there is at least one character in the string.
print("a1b2c3".isalnum())
print("a1b2c3 ".isalnum())
print("a1b2c3+".isalnum())
# >>> True
# >>> False
# >>> False
#
# 2. Similarly,
#   str.isalpha()
#   str.isnumeric()
