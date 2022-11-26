"""
Converts a string to kebab case.
"""
import re


def kebab(s):
    # match all words in the string with lowercase
    s = re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+"
               r"[0-9]*|[A-Z]|[0-9]+",
               lambda mo: ' ' + mo.group(0).lower(), s)
    # replace any - or _ with a space
    s = re.sub(r"(\s|_|-)+", " ", s)
    # combine all word using - as the separator
    s = '-'.join(s.split())
    return s


print(kebab('camelCase'))
# >>> 'camel-case'
print(kebab('some text'))
# >>> 'some-text'
print(kebab('some-mixed_string With spaces_underscores-and-hyphens'))
# >>> 'some-mixed-string-with-spaces-underscores-and-hyphens'
print(kebab('AllThe-small Things'))
# >>> 'all-the-small-things'

# -------------------- more --------------------
print('-' * 40)

# 1. Naming Convention:
#   Camel Case, Kebab Case, Snake Case, etc.
#
# Camel Case：
#   The first letter of the first word of the variable name to be formed
#   by the combination of 2 or more words is written adjacently, with the
#   first letter of the second word capitalized, e.g., camelCase.
# Kebab Case:
#   It is written by separating the words of the variable name to be
#   created with a "-" character, e.g., kebab-case.
# Snake Case:
#   It is written by separating the words or characters that will make up
#   the variable name with a "_" character, e.g., snake_case.
#
# 2. def sub(pattern, repl, string, count=0, flags=0):
#        repl can be either a string or a callable;
#        if a string, backslash escapes in it are processed. If it is
#        a callable, it's passed the Match object and must return a
#        replacement string to be used.
res = re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+"
             r"[0-9]*|[A-Z]|[0-9]+",
             lambda x: x.group(0).lower(), "The Bigger One")
print(res)
# >>> the bigger one
#
print('-' * 40)
# 3. The groups() & re.MatchObject.group() method in regular expressions
# (1) groups()
#   This method returns a tuple containing all the subgroups of the match,
#   from 1 up to however many groups are in the pattern.
# (2) re.MatchObject.group([n])
#   This method returns the complete matched subgroup by default or a tuple
#   of matched subgroups depending on the number of arguments.
#   n: (optional) n defaults to zero (meaning that it it will return the
#   complete matched string)

match_object = re.match(r'(\w+)@(\w+)\.(\w+)', 'username@geekforgeeks.org')

# for the entire match
print(match_object.group())
print(match_object.group(0))

# for the first parenthesized subgroup
print(match_object.group(1))

# for the second parenthesized subgroup
print(match_object.group(2))

# for the third parenthesized subgroup
print(match_object.group(3))

# for a tuple of all matched subgroups
print(match_object.group(1, 2, 3))
print(match_object.groups())
