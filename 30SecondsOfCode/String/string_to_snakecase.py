"""
Converts a string to snake case.
"""
from re import sub


def snake(s):
    s = s.replace('-', ' ')
    s = sub('([A-Z]+)', r' \1', s)
    s = sub('([A-Z][a-z]+)', r' \1', s)
    s = '_'.join(s.split()).lower()
    return s


print(snake('camelCase'))
# >>> 'camel_case'
print(snake('some text'))
# >>> 'some_text'
print(snake('some-mixed_string With spaces_underscores-and-hyphens'))
# >>> 'some_mixed_string_with_spaces_underscores_and_hyphens'
print(snake('AllThe-small Things'))
# >>> 'all_the_small_things'
