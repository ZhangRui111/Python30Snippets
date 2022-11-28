import re

# II-1. re.compile()
print('-' * 20, "re.compile()", '-' * 20)

pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)  # None
m = pattern.match('one12twothree34four', pos=2, endpos=10)
print(m)  # None
m = pattern.match('one12twothree34four', pos=3, endpos=10)
print(m)  # 匹配成功，返回一个 Match 对象：
print(m.start())  # matchObj.start(): 匹配字符串起始位置
print(m.end())  # matchObj.end(): 匹配字符串结束位置
print(m.span())  # matchObj.span(): 匹配字符串位置
print(m.group(0))   # 匹配字符串内容
# None
# None
# <re.Match object; span=(3, 5), match='12'>
# 3
# 5
# (3, 5)
# 12

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
m = pattern.search('Hello World Wide Web')
if m:
    print(m.group(0))
    print(m.span(0))
    print(m.group(1))
    print(m.span(1))
    print(m.group(2))
    print(m.span(2))
    try:
        print(m.group(3))
    except IndexError as err:
        print("IndexError", err)
else:
    print('Nothing found!')
# Hello World
# (0, 11)
# Hello
# (0, 5)
# World
# (6, 11)
# IndexError no such group

# II-2. re.match()
print('-' * 20, "re.match()", '-' * 20)

print(re.match('www', 'www.runoob.com').span())
print(re.match('com', 'www.runoob.com'))
# (0, 3)
# None

matchObj = re.match(r'(.*) are (.*?) .*', "Cats are smarter than dogs",
                    flags=re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
    print("matchObj.span() : ", matchObj.span())
else:
    print("No match!!")
# matchObj.group() :  Cats are smarter than dogs
# matchObj.group(1) :  Cats
# matchObj.group(2) :  smarter
# matchObj.groups() :  ('Cats', 'smarter')
# matchObj.span() :  (0, 26)

# II-3. re.search()
print('-' * 20, "re.search()", '-' * 20)

print(re.search('www', 'www.runoob.com').group(0))
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').group(0))
print(re.search('com', 'www.runoob.com').span())
# www
# (0, 3)
# com
# (11, 14)

searchObj = re.search(r'(.*) are (.*?) .*', "Cats are smarter than dogs",
                      flags=re.M | re.I)
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
    print("matchObj.groups() : ", matchObj.groups())
else:
    print("Nothing found!!")
# searchObj.group() :  Cats are smarter than dogs
# searchObj.group(1) :  Cats
# searchObj.group(2) :  smarter
# matchObj.groups() :  ('Cats', 'smarter')

# II-4. re.sub()
print('-' * 20, "re.sub()", '-' * 20)

phone = "2004-959-559 # 这是一个国外电话号码"
num = re.sub(r'#.*$', "", phone)  # 删除字符串中的 Python注释
print(num)
num = re.sub(r'\D', "", phone)  # 删除非数字(-)的字符串
print(num)
# 2004-959-559
# 2004959559


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
# A46G8HFD1134

# II-5. pattern.findall()
print('-' * 20, "pattern.findall()", '-' * 20)

pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print(result1)
print(result2)
# ['123', '456']
# ['88', '12']

result = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(result)
# [('width', '20'), ('height', '10')]

# II-6. re.finditer()
print('-' * 20, "re.finditer()", '-' * 20)

it = re.finditer(r"\d+", "12a32bc43jf3")
for match in it:
    print(match.group())
# 12
# 32
# 43
# 3

# II-6. re.split()
print('-' * 20, "re.split()", '-' * 20)

print(re.split('\W+', 'runoob, runoob, runoob.'))
# ['runoob', 'runoob', 'runoob', '']
print(re.split('(\W+)', 'runoob, runoob, runoob.'))
# ['runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
print(re.split('\W+', 'runoob, runoob, runoob.', maxsplit=1))
# ['runoob', 'runoob, runoob.']
