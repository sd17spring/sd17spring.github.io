---
date: '2017-01-26'
description: String formatting
published: false
title: Day 4
---

**Today**

* Reading journal debrief
* Sharing lessons learned on unit testing
* String formatting
* Open studio time

**For next time**

* Reading Journal, Think Python chapter 10
* Read [AmGit Chapter 3](https://github.com/AllenDowney/amgit/blob/master/en/03-git-branching/01-chapter3.markdown) and [Chapter 4](https://github.com/AllenDowney/amgit/blob/master/en/04-git-server/01-chapter4.markdown)
* Review [Linux at Olin](https://docs.google.com/viewer?a=v&pid=sites&srcid=ZGVmYXVsdGRvbWFpbnxzZDE1c3ByaW5nfGd4OmMyNzcyOTBjYThlMTM1Mg) if you didn't get a chance previously

## Reading Journal Debrief

We'll be going over your [compiled
answers](http://nbviewer.jupyter.org/github/paulruvolo/SoftDesSp16Prep/blob/master/processed_notebooks/day3_ reading_journal_ responses.ipynb).


## Sharing Lessons Learned on Unit Testing

As a class, we will have a discussion on unit testing.

1. In what ways have you found unit tests helpful?
2. What role does unit testing play in determining whether or not your program is correct? This may vary depending on the program.
3. Any aspects of unit testing that you find unwieldy?
4. Any lessons or best practices to share with the class?


## String Formatting

Now that you've been playing with strings for a while, there are a few
additional tricks that may help you deal with them. You already know several
ways to manipulate strings:

* Concatenation `+`
* Multiplication `*`
* Slicing `[]`
* String methods (e.g. `split`, `upper`)

```
>>> excited = "Software " + "Design" + "!"*10
>>> print(excited)
Software Design!!!!!!!!!!
>>> bored = excited.rstrip("!")
>>> print(bored)
Software Design
>>> print(bored[-6:])
Design
>>> print(bored.split())
['Software', 'Design']
```

Python also has several other built-in facilities for formatting strings.
Among other things, this makes it much easier to create things like your
square root table!

There are two main ways to format strings in Python, and you're likely to see
both in code you read.

The [older method](https://docs.python.org/2/library/stdtypes.html#string-formatting) uses a format string and the percent character (same as the modulo
operator) to replace pieces of the format string. For example, to insert an
integer, you could use:

```
>>> print "Your number is %d" % 52
Your number is 52
```

The [newer method](https://docs.python.org/2/library/string.html#format-string-syntax) also uses a (similar) format string, but uses an explicit
format method:

```
>>> print "Your number is {:d}".format(52)
Your number is 52
```

In my opinion, the newer method can have a bit more complex syntax, but is
often clearer and can be far more powerful.

The documentation for each can be a bit dense, but fortunately there is a
great cheat sheet with useful tasks at <https://pyformat.info>


**Exercise: cheap is $33, free is $34 !**

You walk into a store where each item is priced according to the letters in
its name: 'a' costs $1, 'b' is $2, and so on. Write a program that prints a
receipt for this wacky store:

```
bananas $52
rice $35
paprika $72
potato chips $78
------------------------

Total $237
```

What helper functions would be useful in creating this receipt program?

Hint: the [built-in 'ord' and
'chr'](https://docs.python.org/2/library/functions.html) functions may be
useful. If you use these, pay attention to how case affects the result.
