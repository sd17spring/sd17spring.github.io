---
date: 2017-01-29
description: ''
title: Word Frequency Analysis
---

{% include toc %}

This exercise has been adapted from Think Python Ch. 13.1. The goal of this
toolbox exercise will be to write a Python program that can automatically
analyze the linguistic characteristics of a book. Along the way we will learn
a bit about reading files.

## Get Set

Grab the starter code for this toolbox exercise via the normal fork-and-clone
method from <https://github.com//{{site.course.github_owner}}/ToolBox-WordFrequency>

The starter code will be in `frequency.py`.

## Download your favorite book

Go to Project Gutenberg (`<http://gutenberg.org>`) and download your favorite
out-of-copyright book in plain text format. The file `pg32325.txt` has
been placed in the `word_frequency_analysis` directory to give you an example of
the type of file you should download.

## Complete the declared function `get_word_list`

The function should read the specified Project Gutenberg text file, strip out
whitespace, header comments, and punctuation and return a list of all words in
the book in order. In addition, the words should all be converted to
lowercase.

Hints:

"The `string` module provides strings named `whitespace`, which contains
space, tab, newline, etc., and `punctuation` which contains the punctuation
characters. Let’s see if we can make Python swear:

    >>> import string
    >>> print(string.punctuation)
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

Also, you might consider using the string methods `strip`, `replace`,
`split`, and `translate`. -- Think Python 12.1.

_More Hints:_

The first step is loading the file and stripping away the header comment. Here
is some code that does just this and stores the resultant list of lines in a
variable called `lines`. Make sure you understand what it is doing, and modify
it if you need to:

``` python
f = open(file_name,'r')
lines = f.readlines()
curr_line = 0
while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
  curr_line += 1
  lines = lines[curr_line+1:]
```

## Get Top 100 Words

Next, fill out the implementation of the function `get_top_n_words` that takes
as input the list of words computed in by your `get_word_list function` and
searches for the n most frequently used words and returns a list of these
words in order of frequency from most to least frequently occurring.

Hints: you will probably want to process the raw list of words into a
dictionary where the key is a particular word and the value is the number of
times it occurs in the input `word_list`. Suppose you have created such a
dictionary and its name is `word_counts`. You can sort the words by frequency
of occurrence using the Python code:

`ordered_by_frequency = sorted(word_counts, key=word_counts.get, reverse=True)`

## Finishing your program

Add some code that calls the two functions you just wrote so that you get the
words in your Project Gutenberg text, calculate the top 100 most frequently
occurring words, and print the word list out. Once you have done this, push
your finished code to your repository and submit a pull request to get your
toolbox exercise checked off with a NINJA.

## (optional) Making it Cooler

If you want to do some more advanced word frequency analysis, try the rest of
the exercises in Think Python 13.1.
