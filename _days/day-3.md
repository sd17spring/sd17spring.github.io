---
title: Day 3
date: 2017-01-24 00:00:00 -05:00
activity_date: 2017-01-24
description: Exploring modular design, intro to unit testing
---

## Today

* Gene Finder guest lecture by Joanne Pratt
* Reading journal day 1 debrief
* Exploring modular design
* Intro to unit testing

## For Next Time

* Start on mini-project 1
* Read _Think Python_ Ch. 8, 10.1-10.6.
* Do the reading journal.

## Reading Journal Day 1 Debrief

We'll go over some of the take homes from [the reading
journals]({{site.data.course.urls.reading_journal_response_prefix}}day1_reading_journal_responses.ipynb) that we collected from the class.

The [day 2 reading
journal responses]({{site.data.course.urls.reading_journal_response_prefix}}day2_reading_journal_responses.ipynb) are also now available.

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

2\. Modify your function to take in two additional inputs that specify the
dimensions of width and height (in characters) of each of the boxes that
compose the grid. For instance,

`grid(6, 3)` produces

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

## Running doctests

Doctests can be run in normal mode, in which only _failing_  tests will be
reported, or in verbose mode, which reports results from all tests.

If you've written a program called `my_prog.py`, you can test it from the
command line by running

``` bash
$ python3 -m doctest [-v] my_prog.py
```

where the `[-v]` means you can either include the `-v` verbose flag or not.

You can also run doctests from inside your program, by including:

``` python
import doctest
doctest.testmod(verbose=True)
```

at the bottom.

**Exercise** : Add doctests to your `is_triangle` function from the Day 1 reading journal and verify your implementation.
