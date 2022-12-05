"""
Converts a given string into a list of words.
"""
import re


def words(s, pattern=r'[a-zA-Z-]+'):
    return re.findall(pattern, s)


print(words('I love Python!!'))
# >>> ['I', 'love', 'Python']
print(words('python, javaScript & coffee'))
# >>> ['python', 'javaScript', 'coffee']

# -------------------- more --------------------
# https://www.cnblogs.com/litmmp/p/4925374.html
print("\\b in regular expression")
print(words('build --out some-item one- -two -three-', r'[a-zA-Z-]+'))
# >>> ['build', '--out', 'some-item', 'one-', '-two', '-three-']
print(words('build --out some-item one- -two -three-', r'\b[a-zA-Z-]+'))
# >>> ['build', 'out', 'some-item', 'one-', 'two', 'three-']
print(words('build --out some-item one- -two -three-', r'[a-zA-Z-]+\b'))
# >>> ['build', '--out', 'some-item', 'one', '-two', '-three']
print(words('build --out some-item one- -two -three-', r'\b[a-zA-Z-]+\b'))
# >>> ['build', 'out', 'some-item', 'one', 'two', 'three']
