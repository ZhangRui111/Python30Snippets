"""
How do I convert a string to lowercase in Python?
"""
# str.lower()
#   Python's standard method for converting a string to lowercase is
#   str.lower() and is compatible with both Python 2 and Python 3. While
#   this is the standard way for most cases, there are certain cases where
#   this method might not be the most appropriate, especially if you are
#   working with Unicode strings.
print('Hello'.lower())
# 'hello'
print('Straße'.lower())
# 'straße'
print('Straße'.upper().lower())
# 'strasse'
# Example of incorrect result when used for unicode case-insensitive matching
print('Straße'.upper().lower() == 'Straße'.lower())
# False ('strasse' != 'straße')

# str.casefold()
#   Python 3 introduced str.casefold(), which is very similar to str.lower(),
#   but stronger, more aggressive as it is intended to remove all case
#   distinctions in Unicode strings.
print('Hello'.casefold())
# 'hello'
print('Straße'.casefold())
# 'strasse'
print('Straße'.upper().casefold())
# 'strasse'
# Returns the correct result when used for unicode case-insensitive matching
print('Straße'.upper().casefold() == 'Straße'.casefold())
# True

# -------------------- more --------------------
# upper()
# The upper() method returns a string where all characters are in upper case.
# Symbols and Numbers are ignored.
print("Hello my friends".upper())  # HELLO MY FRIENDS
# title()
# The title() method converts the first character in each word to uppercase
# and the remaining characters to lowercase in the string and returns a new
# string.
print("Hello my friends".title())  # Hello My Friends
