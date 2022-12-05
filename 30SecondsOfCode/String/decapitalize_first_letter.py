"""
Decapitalizes the first letter of a string.
"""


def decapitalize_first_letter(s, upper_rest=False):
    # Omit the upper_rest parameter to keep the rest of the string intact,
    # or set it to True to convert to uppercase.
    return ''.join([s[0].lower(), (s[1:].upper() if upper_rest else s[1:])])


print(decapitalize_first_letter('FooBar'))
# >>> 'fooBar'
print(decapitalize_first_letter('FooBar', True))
# >>> 'fOOBAR'
