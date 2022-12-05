"""
Splits a multiline string into a list of lines.
"""


def split_lines(s):
    return s.split('\n')


print(split_lines('\nThis\nis a\nmultiline\nstring\n'))
# >>> ['', 'This', 'is a', 'multiline', 'string', '']
print('\nThis\nis a\nmultiline\nstring\n'.splitlines())
# >>> ['', 'This', 'is a', 'multiline', 'string']
