# Python正则表达式 (Python Regular Expression)

> [菜鸟教程](https://www.runoob.com/python/python-reg-expressions.html)

## I. 正则表达式模式与实例

1. 模式
- 字母和数字匹配自身；多数字母和数字前加一个反斜杠 (转义符) 时会拥有不同的含义。
- 标点符号表示特殊的含义；标点符号前加一个反斜杠 (转义符) 时才匹配自身。
- 反斜杠本身需要使用反斜杠转义。
- 由于正则表达式通常都包含反斜杠，所以最好使用原始字符串来表示它们，即，`r"\d+"`。

2. 实例
- `python`: 匹配 "python"
- `[Pp]ython`: 匹配 "Python" 或 "python"
- `rub[ye]`: 匹配 "ruby" 或 "rube"
- `[aeiou]`: 匹配中括号内的任一字母
- `[^aeiou]`: 除了aeiou字母以外的任一字符
- `[0-9]`: 匹配任一数字。类似于 `[0123456789]`
- `[^0-9]`: 匹配除了数字外的任一字符
- `[a-z]`: 匹配任一小写字母
- `[A-Z]`: 匹配任一大写字母
- `[a-zA-Z0-9]`: 匹配任一字母及数字
  

- `.`: 匹配除换行符 "\n" 之外的任何单个字符。要匹配包括 "\n" 在内的任何字符，
  请使用象 `[.\n]` 的模式
- `^`: 匹配字符串的开头
- `$`: 匹配字符串的末尾
- `re*`: 匹配0个或多个的表达式
- `re+`: 匹配1个或多个的表达式
- `re?`: 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
- `re{n}`: 精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能
  匹配 "food" 中的两个 o
- `re{n,}`: 匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 
  "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"
- `re{n, m}`: 匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
- `a | b`: 匹配a或b
- `(re)`: 对正则表达式分组并记住匹配的文本
- `\d`: 匹配一个数字字符。等价于 `[0-9]`
- `\D`: 匹配一个非数字字符。等价于 `[^0-9]`
- `\s`: 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 `[ \f\n\r\t\v]`
- `\S`: 匹配任何非空白字符。等价于 `[^ \f\n\r\t\v]`
- `\w`: 匹配包括下划线的任何单词字符。等价于`[A-Za-z0-9_]`
- `\W`: 匹配任何非单词字符。等价于 `[^A-Za-z0-9_]`
- `\b`: 匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 
  中的 'er'，但不能匹配 "verb" 中的 'er'
- `\B`: 匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'
- `\1...\9`: 匹配第n个分组的内容，例如，`sub('([A-Z]+)', r' \1', "camelCase")`，
  第一个分组`([A-Z]+)` 匹配到 'Case'，`r' \1'` 会在 'Case' 前加一个空格，字符串变为
  "camel Case"

## II. 常用的正则表达式处理函数

Python 的 re 模块支持正则表达式功能

1. re.compile()

   功能: 用于编译正则表达式，生成一个正则表达式 (Pattern/RegexObject) 对象，
   可用于进一步调用 pattern.match/search/findall/finditer/split/sub/...等函数。

   语法: `re.compile(pattern[, flags])`

   其他:
      - pattern.match/search/findall/finditer/... 都有可选的用于指定字符串位置的
        参数: `pos` 和 `endpos`，但不再具有 `flag` 参数。
      - 语法: `pattern.match/search/findall/finditer/...(string: AnyStr[, 
        pos: int[, endpos: int]])`
         - pos: 可选参数，指定字符串的起始位置，默认为 0。
         - endpos: 可选参数，指定字符串的结束位置，默认为字符串的长度。

2. re.match()
   
   功能: re.match 尝试从字符串的<u>起始位置</u>匹配一个模式，成功匹配则返回一个
   MatchObject 对象；如果不是起始位置匹配成功的话，match() 就返回 None。 
   
   语法: `re.match(pattern, string[, flags=0])`
      - flags: 标志位，用于控制正则表达式的匹配方式。参见"正则表达式修饰符 - 
        可选标志"。
   
   其他:
      - `pattern.match(string: AnyStr[, pos: int[, endpos: int]])`
   
3. re.search()

   功能: re.search 扫描整个字符串并返回<u>第一个</u>成功的匹配，成功匹配则返回
   一个 MatchObject 对象，否则返回None。

   语法: `re.search(pattern, string[, flags=0])`

   其他: 
      - re.match与re.search的区别
      - `pattern.search(string: AnyStr[, pos: int[, endpos: int]])`
   
4. re.sub()

   功能: 替换字符串中的匹配项，返回替换后的字符串。

   语法: `re.sub(pattern, repl, string[, count=0, flags=0])`
      - repl: 替换的字符串，也可为一个函数。
      - count: 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
   
   其他:
      - `pattern.sub(repl: AnyStr, string: AnyStr[, count: int])`

5. re.findall()

   功能: 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，
   则返回元组列表，如果没有找到匹配的，则返回空列表。

   语法: `re.findall(pattern, string[, flags=0])`

   其他:
      - match 和 search 是匹配一次，findall 匹配所有。
      - `pattern.findall(string: AnyStr[, pos: int[, endpos: int]])`
   
6. re.finditer()

   功能: 和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。

   语法: `re.finditer(pattern, string[, flags=0])`

   其他:
      - `pattern.finditer(string: AnyStr[, pos: int[, endpos: int]])`
   
7. re.split()

   功能: split 方法按照能够匹配的子串将字符串分割后返回列表。

   语法: `re.split(pattern, string[, maxsplit=0, flags=0])`
      - maxsplit: 分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。

   其他:
      - 对于一个找不到匹配的字符串而言，split 不会对其作出分割。
      - `pattern.split(string: AnyStr[, maxsplit: int])`
   
## III. 其他

### 1. 正则表达式对象
- re.RegexObject 
  re.compile() 返回 RegexObject 对象。
  
- re.MatchObject  
   - groups()
   - group(num=0)。
   - start(num=0)
   - end(num=0)
   - span(num=0)
   
   注意: span(num), start(num) 和 end(num) 的参数 num 跟 group(num) 中的 num 类似，
  可以指定第 num 个分组匹配成功的子串。

### 2. 正则表达式修饰符 - 可选标志
多个标志可以通过按位 OR(|) 来指定
- re.I: 忽略大小写
- re.L: 做本地化识别 (locale-aware) 匹配，即，特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
- re.M: 多行匹配，影响 ^ 和 $
- re.S: 使 . 匹配包括换行在内的所有字符
- re.U: 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B, \d, \D, \s, \S
- re.X: 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解，即，为了增加可读性，忽略空格和 # 后面的注释
