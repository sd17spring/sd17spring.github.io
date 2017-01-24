---
date: '2017-01-24'
description: Exploring modular design, intro to unit testing
title: Day 3
---

## Today

* Gene Finder guest lecture by Joanne Pratt
* Reading journal day 1 debrief
* Exploring modular design
* Intro to unit testing

## For Next Time

* Start on mini-project 1

## Reading Journal Day 1 Debrief

We'll go over some of the take homes from [the reading
journals]({{site.data.course.urls.reading_journal_response_prefix}}day1_reading_journal_responses.ipynb) that we collected from the class.

## Exploring Modular Design

In groups of 3, review the [solutions from the class]({{site.data.course.urls.reading_journal_response_prefix}}day1_reading_journal_responses.ipynb##Exercise-3.3) to the Exercise 3.3.

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

## Running doctests

Doctests can be run in normal mode, in which only _failing_  tests will be
reported, or in verbose mode, which reports results from all tests.

If you've written a program called `my_prog.py`, you can test it from the
command line by running

``` bash
$ python3 -m doctest [-v] my_ prog.py
```

where the `[-v]` means you can either include the `-v` verbose flag or not.

You can also run doctests from inside your program, by including:

``` python
import doctest
doctest.testmod(verbose=True)
```

at the bottom.

**Exercise** : Add doctests to your `is_triangle` function from the Day 1 reading journal and verify your implementation.
