# Python标准库速查表

**PS**: **README.md为最新文档！**

使用Python v3.7.4

- [中文](README-zh-cn.md)
- [English](README.md)

**注意**:
- **这里的每个代码片段都可以独立运行**
- **如果你希望复制代码，请使用[command to code](https://pynickle.github.io/ctc.html)**
- **你可以使用GETREADME.py来从仓库中下载README.md**

## 目录

**文本处理**: [``string``](#string), [``re``](#re), [``difflib``](#difflib),
[``textwrap``](#textwrap), [``unicodedata``](#unicodedata)

**二进制数据**: [``codecs``](#codecs)

**数据类型**: [``datetime``](#datetime), [``calendar``](#calendar), [``collections``](#collections),[``copy``](#copy), [``pprint``](#pprint), [``enum``](#enum)
     
**数学模块**: [``math``](#math), [``cmath``](#cmath), [``random``](#random)

**函数式编程**: [``itertools``](#itertools), [``functools``](#functools)

**目录访问**: [``pathlib``](#pathlib), [``os.path``](#os.path), [``glob``](#glob)

**数据持久化**: [``pickle``](#pickle)

**数据压缩**: [``zlib``](#zlib), [``lzma``](#lzma)

**加密服务**: [``hashlib``](#hashlib), [``hmac``](#hmac), [``secrets``](#secrets)

**操作系统**: [``os``](#os), [``time``](#time), [``logging``](#logging),
[``getpass``](#getpass),  [``platform``](#platform)

**互联网数据**: [``json``](#json)

**结构化标记**: [``html``](#html)

**开发工具**: [``typing``](#typing)

**调试和分析**: [``timeit``](#timeit), [``pdb``](#pdb)

**运行时服务**: [``sys``](#sys)

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

## codecs

#### encode, decode, getencoder, getdecoder

```python
>>> import codecs
>>> codecs.encode("你好")
b'\xe4\xbd\xa0\xe5\xa5\xbd'
>>> codecs.decode(b"\xe4\xbd\xa0\xe5\xa5\xbd")
'你好'
>>> codecs.getencoder("utf-8")
<built-in function utf_8_encode>
>>> codecs.getdecoder("gbk")
<built-in method decode of MultibyteCodec object at 0x0000019E080AA078>
```

## datetime

#### MINYEAR, MAXYEAR, date

```python
>>> import datetime
>>> datetime.MINYEAR
1
>>> datetime.MAXYEAR
9999
>>> date = datetime.date
>>> date.today()
datetime.date(2019, 7, 21)
>>> date = datetime.date(2019, 7, 21)
>>> date.today()
datetime.date(2019, 7, 21)
>>> date.weekday()
6
>>> date.isocalendar()
(2019, 29, 7)
>>> date.ctime()
'Sun Jul 21 00:00:00 2019'
>>> date.strftime("%Y %d %y, %H:%M:%S")
'2019 21 19, 00:00:00'
```

## calendar

#### isleap, firstweekday, month

```python
>>> import calendar
>>> calendar.isleap(2000)
True
>>> calendar.firstweekday()
0
>>> print(calendar.month(2019, 7))
     July 2019
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30 31
```

## collections

#### namedtuple, deque, defaultdict, OrderedDict, Counter

```python
>>> import collections
>>> point = collections.namedtuple("point", ["x", "y"])
>>> p = point(2, 1)
>>> p.x, p.y
(2, 1)
>>> deque = collections.deque(["b", "c", "d"])
>>> deque.appendleft("a")
>>> deque.append("e")
>>> deque
deque(['a', 'b', 'c', 'd', 'e'])
>>> dd = collections.defaultdict(lambda: "None")
>>> dd ["key-1"] = "value-1"
>>> dd["key-1"]
'value-1'
>>> dd["key-2"]
'None'
>>> od = collections.OrderedDict([("a", 1), ("b", 2)])
>>> od
OrderedDict([('a', 1), ('b', 2)])
>>> c = collections.Counter()
>>> for i in "Hello, World":
...     c[i] = c[i] + 1
...
>>> c
Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ',': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
```

## copy

#### copy, deepcopy

```python
>>> import copy
>>> origin = [1, 2, [3, 4]]
>>> copy1 = copy.copy(origin)
>>> copy2 = copy.deepcopy(origin)
>>> copy1 is copy2
False
>>> origin[2][0] = "Hello, copy"
>>> copy1
[1, 2, ['Hello, copy', 4]]
>>> copy2
[1, 2, [3, 4]]
```

## pprint

#### pprint

```python
>>> import pprint
>>> strcmp = ("hello world", {"nick": 13, "ben": 12}, (1, 2, 3, 4), [5, 6, 7, 8], "Hello pprint")
>>> pprint.pprint(strcmp)
('hello world',
 {'ben': 12, 'nick': 13},
 (1, 2, 3, 4),
 [5, 6, 7, 8],
 'Hello pprint')
```

## enum

#### Enum, unique, auto

```python
>>> import enum
>>> class Seasons(enum.Enum):
...     Spring = 1
...     Summer = 2
...     Autumn = 3
...     Winter = 4
...
>>> Seasons.Spring
<Seasons.Spring: 1>
>>> @enum.unique
... class Unique(enum.Enum):
...     Nick = 13
...     Ben = 12
...     Jack = 13
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "C:\Python38\lib\enum.py", line 860, in unique
    raise ValueError('duplicate values found in %r: %s' %
ValueError: duplicate values found in <enum 'Unique'>: Jack -> Nick
>>> class Auto(enum.Enum):
...     VS = enum.auto()
...     VSCode = enum.auto()
...     Pycharm = enum.auto()
...
>>> list(Auto)
[<Auto.VS: 1>, <Auto.VSCode: 2>, <Auto.Pycharm: 3>]
```

## math

#### ceil, factorial, floor, modf, log, pow, sqrt, pi, e

```python
>>> import math
>>> math.ceil(1.4)
2
>>> math.factorial(5)
120
>>> math.floor(1.6)
1
>>> math.modf(1.6)
(0.6000000000000001, 1.0)
>>> math.log(8)
2.0794415416798357
>>> math.pow(2,5)
32.0
>>> math.sqrt(9)
3.0
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
```

## cmath

#### sin, tan, cos

```python
>>> import cmath
>>> cmath.sin(7)
(0.6569865987187891+0j)
>>> cmath.tan(7)
(0.8714479827243188+0j)
>>> cmath.cos(7)
(0.7539022543433046-0j)
```

## random

#### random, uniform, randint, randrange

```python
>>> import random
>>> random.random()
0.6381052887323486
>>> random.uniform(5,6)
5.325285695528384
>>> random.randint(6, 9)
9
>>> random.randrange(5, 10)
9
```

## itertools

#### count, repeat, groupby

```python
>>> import itertools
>>> for i in zip(itertools.count(1), ["A", "B", "C"]):
...     print(i)
...
(1, 'A')
(2, 'B')
(3, 'C')
>>> for i in itertools.repeat("Hello Repeat!", 5):
...     print(i)
...
Hello Repeat!
Hello Repeat!
Hello Repeat!
Hello Repeat!
Hello Repeat!
>>> [list(g) for k, g in itertools.groupby('AAAABBBCCD')]
[['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]
```

## functools

####

```python
>>> import functools
>>> @functools.lru_cache(None)
... def fibonacci(n):
...     if n<2:
...         return n
...     return fibonacci(n-1) + fibonacci(n-2)
...
>>> fibonacci(10)
55
>>> def add(a, b):
...     return a+b
...
>>> functools.reduce(add, range(1,100))
4950
```

## pathlib

#### Path

```python
>>> import pathlib
>>> p = pathlib.Path(".")
>>> list(p.glob('**/*.py'))
[WindowsPath('GETREADME.py')]
>>> p/"dir"
WindowsPath('dir')
>>> (p/"GETREADME.py").name
'GETREADME.py'
>>> p.is_absolute()
False
```

## os.path

#### exists, getsize, isfile, isdir, join

```python
>>> import os.path
>>> os.path.exists(".")
True
>>> os.path.getsize("./README.md")
11285
>>> os.path.isfile("./README.md")
True
>>> os.path.isdir("./doc")
False
>>> os.path.join("./doc", "tutorial", "basic")
'./doc\\tutorial\\basic'
```

## glob

#### glob

```python
>>> import glob
>>> glob.glob("*.md", recursive = True)
['python-cheatsheet.md', 'README.md']
```

## pickle

#### loads, dumps

```python
>>> import pickle
>>> data = [[1, "first"],
...         [2, "second"]]
>>> dumps = pickle.dumps(data)
>>> dumps
b'\x80\x03]q\x00(]q\x01(K\x01X\x05\x00\x00\x00firstq\x02e]q\x03(K\x02X\x06\x00\x00\x00secondq\x04ee.'
>>> pickle.loads(dumps)
[[1, 'first'], [2, 'second']]
```

## zlib

#### compress, decompress

```python
>>> import zlib
>>> zlib.compress(b"Hello World!", 5)
b'x^\xf3H\xcd\xc9\xc9W\x08\xcf/\xcaIQ\x04\x00\x1cI\x04>'
>>> zlib.decompress(b'x^\xf3H\xcd\xc9\xc9W\x08\xcf/\xcaIQ\x04\x00\x1cI\x04>')
b'Hello World!'
```

## lzma

#### compress, decompress

```python
>>> import lzma
>>> lzma.compress(b"Hello, python3!")
b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x0eHello, python3!\x00\x00(\x92K\xe6\x9b\xe7r&\x00\x01'\x0f\xdf\x1a\xfcj\x1f\xb6\xf3}\x01\x00\x00\x00\x00\x04YZ"
>>> lzma.decompress(b"\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x0eHello, python3!\x00\x00(\x92K\xe6\x9b\xe7r&\x00\x01'\x0f\xdf\x1a\xfcj\x1f\xb6\xf3}\x01\x00\x00\x00\x00\x04YZ")
b'Hello, python3!'
```

## hashlib

#### md5

```python
>>> import hashlib
>>> md5 = hashlib.md5()
>>> md5.update(b"Hello World")
>>> md5.block_size
64
>>> md5.digest_size
16
>>> md5.hexdigest()
'b10a8db164e0754105b7a99be72e3fe5'
>>> md5.digest()
b'\xb1\n\x8d\xb1d\xe0uA\x05\xb7\xa9\x9b\xe7.?\xe5'
```

## hmac

#### new, compare_digest

```python
>>> import hmac
>>> msg = b"Hello World"
>>> secret = b"key"
>>> h = hmac.new(secret, msg, digestmod='md5')
>>> h.hexdigest()
'432c3ea3b9a503183f3d1258d9016a0c'
>>> h.digest()
b'C,>\xa3\xb9\xa5\x03\x18?=\x12X\xd9\x01j\x0c'
>>> h2 = hmac.new(secret, b"Hello world", digestmod="md5")
>>> hmac.compare_digest(h.digest(), h2.digest())
False
```

## secrets

#### choice, token_bytes, token_hex

```python
>>> import secrets
>>> secrets.choice("Hello World!")
'd'
>>> secrets.token_bytes(32)
b'\xd7\x98\xba\xc5\x18[/\xeaLx\xdb\x962\x84\xff`(7&\xe6\xae\xd4\x17n,\xc3\x9e\xb0V\x1c\x1d\x99'
>>> secrets.token_hex(16)
'335f8df0cb6dd60a3c41fdba7ccd1a0b'
```

## os

#### name, getcwd

```python
>>> import os
>>> os.name
'nt'
>>> os.getcwd()
'C:\\Users\\Nick'
```

## time

#### localtime, ctime, perf_counter, sleep, strftime 

```python
>>> import time
>>> time.localtime()
time.struct_time(tm_year=2019, tm_mon=7, tm_mday=29, tm_hour=12, tm_min=18, tm_sec=57, tm_wday=0, tm_yday=210, tm_isdst=0)
>>> time.ctime()
'Mon Jul 29 12:19:40 2019'
>>> time.perf_counter()
174.1987535
>>> time.sleep(1)
>>> time.strftime("%d %b %Y")
'29 Jul 2019'
```

## logging

#### log, info, debug, warning, error, critical

```python
>>> import logging
>>> logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
>>> logger = logging.getLogger(__name__)
>>> logger.info("info")
2019-07-29 12:29:59,363 - __main__ - INFO - info
>>> logger.debug("debug")
>>> logger.error("error")
2019-07-29 12:30:26,729 - __main__ - ERROR - error
>>> logger.critical("critical")
2019-07-29 12:30:36,446 - __main__ - CRITICAL - critical
>>> logger.warning("warning")
2019-07-29 12:30:48,815 - __main__ - WARNING - warning
>>> logger.log(35, "log")
2019-07-29 12:31:59,758 - __main__ - Level 35 - log
```

## getpass

#### getpass, getuser

```python
>>> import getpass
>>> password = getpass.getpass()
Password:
>>> password
'xxx'
>>> getpass.getuser()
'Nick'
```

## platform

#### machine, platform, python_compiler, python_version, system

```python
>>> import platform
>>> platform.machine()
'AMD64'
>>> platform.platform()
'Windows-10-10.0.18362-SP0'
>>> platform.python_compiler()
'MSC v.1916 64 bit (AMD64)'
>>> platform.python_version()
'3.7.4'
>>> platform.system()
'Windows'
```

## json

#### dumps, loads

```python
>>> import json
>>> x = json.dumps({"Nick": 13, "Ben": 10})
>>> x
'{"Nick": 13, "Ben": 10}'
>>> json.loads(x)
{'Nick': 13, 'Ben': 10}
```

## html

#### escape, unescape

```python
>>> import html
>>> html.escape("As we all know, 2>1")
'As we all know, 2&gt;1'
>>> html.unescape('As we all know, 2&gt;1')
'As we all know, 2>1'
```

## webbrowser

#### open

```python
>>> import webbrowser
>>> webbrowser.open("https://www.baidu.com")
True
>>> webbrowser.open("www.baidu.com")
True
```

## typing

#### List, NewType

```python
>>> import typing
>>> lst = typing.List[int]
>>> float_lst = typing.List[float]
>>> def foo(x: float, lst: lst)->float_lst:
...     return [x*num for num in lst]
...
>>> foo(1.5, [3, 4, 5])
[4.5, 6.0, 7.5]
>>> ID = typing.NewType("ID", int)
>>> ID(70)
70
```

## timeit

#### timeit, Timer

```python
>>> import timeit
>>> timeit.timeit("[i for i in range(10000)]", number = 1000)
1.0810747999999961
>>> timeit.timeit("lst = []\nfor i in range(10000):\n    lst.append(i)", number = 1000)
1.770644500000003
>>> a = timeit.Timer("[i for i in range(10000)]")
>>> a.timeit(number = 1000)
0.9840328999999883
```

## pdb

#### set_trace

```python
>>> import pdb
>>> def foo():
...     lst = []
...     for i in range(2):
...         pdb.set_trace()
...         lst.append(i)
...     return lst
...
>>> foo()
> <stdin>(5)foo()
(Pdb) p i
0
(Pdb) p lst
[]
(Pdb) n
> <stdin>(3)foo()
(Pdb) list
[EOF]
(Pdb) n
> <stdin>(4)foo()
(Pdb) r
> <stdin>(5)foo()
(Pdb) p i
1
(Pdb) p lst
[0]
(Pdb) q
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in foo
  File "<stdin>", line 5, in foo
  File "C:\Python37\lib\bdb.py", line 88, in trace_dispatch
    return self.dispatch_line(frame)
  File "C:\Python37\lib\bdb.py", line 113, in dispatch_line
    if self.quitting: raise BdbQuit
bdb.BdbQuit
```

## sys

#### exc_info, implementation, maxsize, platform, version

```python
>>> import sys
>>> try:
...     1/0
... except Exception:
...     print(sys.exc_info())
...
(<class 'ZeroDivisionError'>, ZeroDivisionError('division by zero'), <traceback object at 0x000002D8BF38A248>)
>>> sys.implementation
namespace(cache_tag='cpython-37', hexversion=50791664, name='cpython', version=sys.version_info(major=3, minor=7, micro=4, releaselevel='final', serial=0))
>>> sys.maxsize
9223372036854775807
>>> sys.platform
'win32'
>>> sys.version
'3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)]'
```