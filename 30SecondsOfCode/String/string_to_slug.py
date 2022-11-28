"""
Converts a string to a URL-friendly slug.
"""
import re


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)  # 空白字符, _, - 替换为 -
    s = re.sub(r'^-+|-+$', '', s)  # 去除开头或结尾的-
    return s


print(slugify(' Hello_World!'))
print(slugify('Hello World!'))
print(slugify(' -Hello_World!-'))
# >>> 'hello-world'
# >>> 'hello-world'
# >>> 'hello-world'
