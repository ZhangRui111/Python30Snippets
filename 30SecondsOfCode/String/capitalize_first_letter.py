"""
Capitalizes the first letter of a string.
"""


def capitalize_first_letter(s, lower_rest=False):
    # Omit the lower_rest parameter to keep the rest of the string intact,
    # or set it to True to convert to lowercase.
    return ''.join([s[0].upper(), (s[1:].lower() if lower_rest else s[1:])])


print(capitalize_first_letter('fooBar'))
# >>> 'FooBar'
print(capitalize_first_letter('fooBar', True))
# >>> 'Foobar'

# -------------------- more --------------------
# title(): Capitalizes the first letter of every word in a string.
print('hello world!'.title())
# >>> 'Hello World!'
