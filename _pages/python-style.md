---
title: Python Style
date: 2016-12-29 13:26:01 -05:00
permalink: resources/python-style
---

Program Python like a pro! Code in the right-hand column better to employers
and other places you might send your code. It also helps avoid some common
pitfalls. Finally, most of the code you see will use the patterns in the
right-column; practice _writing_ code this way will help you understand code
that you _read_, when you work on a team or with code from cookbooks and other
projects.

| **Anti-Patterns** | **Patterns**
---|---|---
**Conditions** | if condition is True:| if condition:
| if condition is False:| if not condition:
| if condition:
return True
else:
return False| return condition
|  |
**Parentheses and Whitespace** | a =1
a= 1
a=1| a = 1
| f (a, b)| f(a, b)
| if(a == 1)| if a == 1
|  |
**Indexing** | ar[len(ar) - 1]| ar[-1]
|  |
**Iteration** | i = 0
while i &lt; n:
…
i += 1| for i in range(n):
…
| i = start
while i &lt;= stop:
…
i += 1| for i in range(start, stop + 1):
…
| i = 0
while i &lt; n:
…
i += 2| for i in range(0, n, 2):
…
| for i in range(len(s)):
do something with s[i]| for c in s:
do something with c
| for i in range(len(s)):
do something with i and s[i]| for i, c in enumerate(s):
do something with i and c
|  |

Related links:

* [PEP 0008 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
