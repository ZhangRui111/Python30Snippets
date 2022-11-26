"""
Splits a multiline string into a list of lines.
"""


def split_lines(s):
    return s.split('\n')


print(split_lines('This\nis a\nmultiline\nstring.\n'))
# >>> ['This', 'is a', 'multiline', 'string.' , '']
print('This\nis a\nmultiline\nstring.\n'.splitlines())
# >>> ['This', 'is a', 'multiline', 'string.']
