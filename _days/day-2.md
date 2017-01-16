---
date: '2017-01-23'
description: Exploring modular design, intro to unit testing
published: false
title: Day 2
---

**Today**

* Reading journal day 1 debrief
* Exploring modular design
* Ways to run Python code
* Intro to unit testing
* How to get started with day 2 reading
* Overview of mini-project 1

**For next time**

* Fill out the [course entrance survey]({{site.course.entrance_survey_url}}) if you haven't already
* Complete Day 2 (and Day 1) Reading Journal before noon on 1/28
* Finish [setting up your environment](/assignments/setup-your-environment)
* Start on mini-project 1

## Reading Journal Day 1 Debrief

We'll go over some of the take homes from [the reading
journals](http://nbviewer.jupyter.org/github/paulruvolo/SoftDesSp16Prep/blob/master/processed_notebooks/day1_ reading_journal_ responses.ipynb)
that we collected from the class.

## Exploring Modular Design

In groups of 3, review the [solutions from the
class](http://nbviewer.jupyter.org/github/paulruvolo/SoftDesSp16Prep/blob/master/processed_notebooks/day1_ reading_journal_ responses.ipynb)
to the Chapter 3 Exercise 5.

What aspects of these different designs:

* Increased / decreased the readability of code (readability means your ability to easily deduce what the code does, how it works, and whether or not it is correct).
* Increased / decreased the flexibility of the code (flexibility means the ability of this code to be easily modified to satisfy new requirements that may arise.

In groups, redo Chapter 3 Exercise 5 based on the design that your group
decides is most readable and most flexible.

In a surprise move, your manager has asked you to implement two new features
for your program.


1\. Write a function that draws the following grid

```
+ - - - - + - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - + - - - - +
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
|         |         |         |         |         |
+ - - - - + - - - - + - - - - + - - - - + - - - - +
```


2\. Modify your function to take in two additional inputs that specify the
dimensions of width and height (in characters) of each of the boxes that
compose the grid. For instance,

`grid(6, 3)` produces

```
+ - - + - - + - - + - - + - - +
|     |     |     |     |     |
|     |     |     |     |     |
+ - - + - - + - - + - - + - - +
|     |     |     |     |     |
|     |     |     |     |     |
+ - - + - - + - - + - - + - - +
|     |     |     |     |     |
|     |     |     |     |     |
+ - - + - - + - - + - - + - - +
```

## Running Python Code

There are many ways to run the Python code you write:

### Method 1: Interactive Python interpreter

``` bash
$ python
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> print "Hello, SoftDes!"
Hello, SoftDes!
```

There is also an advanced implementation of the interpreter called ipython
that adds some nice extra features.


### Method 2: Jupyter notebooks

This is what you've been using for Reading Journals. Each code cell in the
notebook is essentially a mini interpreter session.


### Method 3: Within IDE/editor

Several integrated development environments/text editors allow you to run
Python code as you write it. The mechanism for doing so varies by editor:
Sublime Text uses ctrl-b (for "build"), and Atom with the "script" package
uses ctrl-shift-b.

A few things to watch out for: when you run code using this method it usually
can't take standard input, so this means you can't use e.g. the `raw_input
`function. Also, if you run an infinite loop it may freeze your editor!


### Method 4: Saved script

Finally, you can save your program as a text file (with a .py extension by
convention) and run it at the command line:

``` bash
$ python my_ script.py`
`"Hello, SoftDes!"`
```

This is the preferred method for all but the very simplest programs, and is
how you will complete all the assignments in this class other than reading
journals.


## Intro to Unit Testing

Testing our functions interactively in the interpreter as we write them is
great for quick tests.

As we move to more advanced functions and programs, we'd like to add several
more features. We might want to save the tests, to run them again as our
implementation changes. We might even want to write the tests ahead of time,
an approach known as **test-driven design** .

Today, we'll write our first **unit tests** . These short tests let us verify
each piece of a program independently, which makes it more likely the entire
program will be correct once we put everything together. You will be writing
more unit tests in mini-project 1, and in all the work you do for this class.

We will be using the [doctest
](https://docs.python.org/2/library/doctest.html)Python module, which makes
code examples in Python
[docstrings](https://www.python.org/dev/peps/pep-0257/) into unit tests
automatically.


### Running doctests

Doctests can be run in normal mode, in which only _failing_  tests will be
reported, or in verbose mode, which reports results from all tests.

If you've written a program called `my_prog.py`, you can test it from the
command line by running

``` bash
$ python -m doctest [-v] my_ prog.py
```

where the `[-v]` means you can either include the `-v` verbose flag or not.

You can also run doctests from inside your program, by including:

``` python
import doctest
doctest.testmod(verbose=True)
```

at the bottom.

**Exercise** : Add doctests to your `is_triangle` function from the Day 1 reading journal and verify your implementation.


## Starting Day 2 Reading Journal

In order to work on the reading journal for Day 2, you'll need to pull in the
new notebook assignment from the upstream class repositories. Instructions are
posted at <https://github.com//{{site.course.github_owner}}/ReadingJournal>.


## Gene Finder Mini-Project Kickoff

We'll go over the basic ideas together.
