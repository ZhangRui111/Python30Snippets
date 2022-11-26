"""
Capitalizes the first letter of a string.
"""


def capitalize(s, lower_rest=False):
    # Omit the lower_rest parameter to keep the rest of the string intact,
    # or set it to True to convert to lowercase.
    return ''.join([s[0].upper(), (s[1:].lower() if lower_rest else s[1:])])


print(capitalize('fooBar'))
# >>> 'FooBar'
print(capitalize('fooBar', True))
# >>> 'Foobar'
