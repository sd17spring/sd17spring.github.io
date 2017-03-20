---
title: Unittest
date: 2017-01-22 00:00:00 -05:00
description: ''
---

Warning: This toolbox exercise involves OOP (Object Oriented Programming), and
therefore may be a bit confusing until that is covered in class.

Unittest is the industry standard testing framework for python.

## Get Set

Unittest should be installed by default with python. To double check that you
have it, you can open a python interpreter and run

    >>> import unittest

If you don't get any errors, it means everything is already there.

To get started, read the first two sections (the intro and 25.3.1) of the
python unittest documentation found
[here](https://docs.python.org/3/library/unittest.html).

## Making your own test cases

Using [script to sort a list and remove negative numbers], create a test suite
to verify that this script has all if the intended functionality.

A few things to keep in mind:

  * methods need to be named `test_something` so that unittest will recognize them as tests.
  * The `setup` method always runs first and the `teardown` method always runs last. They are not required but can be useful.
