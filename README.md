# Python Standard Libraries Cheatsheet

Depend on Python v3.7.4

**Notes**: 
- **Every code snippet here can run independently**
- **If you want to copy the code, use [command to code](https://pynickle.github.io/ctc.html)**

## Contents

Text Processing: [``string``](#string), [``re``](#re), [``difflib``](#difflib)

## string

#### Attributes

```python
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.hexdigits
'0123456789abcdefABCDEF'
>>> string.octdigits
'01234567'
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>> string.whitespace
' \t\n\r\x0b\x0c'
```

#### Formatter

```python
>>> import string
>>> formatter = string.Formatter()
>>> strcmp = "my name is {name}"
>>> dct = {"name": "nick"}
>>> formatter.format(strcmp, **dct)
'my name is nick'
>>> data = ("3")
>>> strcmp = "pi is about {}"
>>> formatter.format(strcmp, *data)
'pi is about 3'
```

#### Template

```python
>>> import string
>>> strcmp = "Hello $World"
>>> t = string.Template(strcmp)
>>> t.substitute({"World": "nick"})
'Hello nick'
>>> t.substitute(World = "nick")
'Hello nick'
>>> class MyTemplate(string.Template):
...     delimiter = "^"
...
>>> strcmp = "Hello ^World"
>>> mytemplate = MyTemplate(strcmp)
>>> mytemplate.substitute(World = "nick")
'Hello nick'
```

## re

#### match, search, findall

```python
>>> import re
>>> strcmp = "www.baidu.com"
>>> re.match("www", strcmp).span()
(0, 3)
>>> re.match("baidu", strcmp)
>>> re.search("baidu", strcmp).span()
(4, 9)
>>> strcmp = "baidu.com/runoob.com"
>>> re.findall("com", strcmp)
['com', 'com']
>>> re.findall("b(.*?).", strcmp)
['', '']
>>> re.findall("b(.*?)c", strcmp)
['aidu.', '.']
```

#### split, sub, escape

```python
>>> import re
>>> re.split(r"\W", "hello,world")
['hello', 'world']
>>> re.sub(r"Boy|Girl", "Human", "boy and girl", flags = re.I)
'Human and Human'
>>> re.escape(r"#$&*+-.^|~")
'\\#\\$\\&\\*\\+\\-\\.\\^\\|\\~'
```

## difflib

#### Differ

```python
>>> import difflib
>>> d = difflib.Differ()
>>> text1 = """difflib
... python version 3.7.4
... difflib version 3.7.4
... this is difflib document
... """
>>> text2 = """difflib
... python version 3.7.3
... this is difflib document
... feature: diff in linux
... """
>>> text1_lines = text1.splitlines()
>>> text2_lines = text2.splitlines()
>>>
>>> list(d.compare(text1_lines, text2_lines))
['  difflib', '- python version 3.7.4', '?                    ^\n', '+ python version 3.7.3', '?                    ^\n', '- difflib version 3.7.4', '  this is difflib document', '+ feature: diff in linux']
```

#### HtmlDiff

```python
>>> import difflib
>>> d = difflib.HtmlDiff()
>>> text1 = """difflib
... python version 3.7.4
... difflib version 3.7.4
... this is difflib document
... """
>>> text2 = """difflib
... python version 3.7.3
... this is difflib document
... feature: diff in linux
... """
>>> text1_lines = text1.splitlines()
>>> text2_lines = text2.splitlines()
>>> with open("HtmlDiff.html", "w", encoding="utf-8") as f:
...     HtmlDiff = d.make_file(text1_lines, text2_lines)
...     f.write(HtmlDiff)
...
3331
```

#### SequenceMatcher

```python
>>> import difflib
>>> s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=0, b=4, size=5)
>>> s = difflib.SequenceMatcher(lambda x: x==" ", " abcd", "abcd abcd")
>>> s.find_longest_match(0, 5, 0, 9)
Match(a=1, b=0, size=4)
>>> s = difflib.SequenceMatcher(None, "abcd", "abd")
>>> s.get_matching_blocks()
[Match(a=0, b=0, size=2), Match(a=3, b=2, size=1), Match(a=4, b=3, size=0)]
```

## textwrap

#### wrap, fill, shorten, dedent, indent

```python
>>> import textwrap
>>> strcmp = "Hello,World! My name is nick, l am 14 years old"
>>> textwrap.wrap(strcmp, width = 10)
['Hello,Worl', 'd! My name', 'is nick, l', 'am 14', 'years old']
>>> textwrap.fill(strcmp, width = 10)
'Hello,Worl\nd! My name\nis nick, l\nam 14\nyears old'
>>> textwrap.shorten(strcmp, width = 45)
'Hello,World! My name is nick, l am 14 [...]'
>>> textwrap.shorten(strcmp, width = 45, placeholder = "...")
'Hello,World! My name is nick, l am 14...'
>>> strcmp = """
...     hello world!
... """
>>> textwrap.dedent(strcmp)
'\nhello world!\n'
>>> strcmp = """Hello World!
... l am nick.
... l am 14 years old.
... """
>>> textwrap.indent(strcmp, " + ", lambda line: True)
' + Hello World!\n + l am nick.\n + l am 14 years old.\n'
```

## unicodedata

#### lookup, name, unidata_version

```python
>>> import unicodedata
>>> unicodedata.lookup('LEFT CURLY BRACKET')
'{'
>>> unicodedata.name("(")
'LEFT PARENTHESIS'
>>> unicodedata.unidata_version
'11.0.0'
```




