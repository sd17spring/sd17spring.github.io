---
title: Day 8
date: 2017-02-13 00:00:00 -05:00
activity_date: 2017-02-12 19:00:00 -05:00
description: Recursion practice, computational art gallery show
---

{% include construction %}

## Today

* Gallery show
* More recursion (Levenshtein distance and memoization).
* Text mining mini-project launch


## For Next Time

* Reading journal, Think Python 13, 15 due Thursday


## More Recursion

Let's circle back on some of the recursion practice problems from last time.
We'll start by implementing Levenshtein distance together as a class. Here is
the description of the problem from last time.

> Write a function called `levenshtein_distance` that takes as input two
strings and returns the [Levenshtein
distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between the two
strings. Intuitively, the Levenshtein distance is the minimum number of edit
operations to transform one string into the other (for this reason Levenshtein
distance is sometimes called "edit distance"). These edits can either be
insertions, deletions, or substitutions. Note that Levenshtein distance is
similar to [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance),
but works for strings of differing lengths

> Here are some examples of these operations:
>
> 1. <tt><b><u>k</u></b>itten</tt> → <tt><b><u>s</u></b>itten</tt> (substitution of `s` for `k`)
> 2. <tt>sitt<b><u>e</u></b>n</tt> → <tt>sitt<b><u>i</u></b>n</tt> (substitution of `i` for `e`)
> 3. <tt>sittin</tt> → <tt>sittin<b><u>g</u></b></tt>  (insertion of `g` at the end).
>
> While this function seems initially daunting, it admits a very compact
recursive solution. You can either work on your own to see the recursive
solution, or use the recursive solution given in the Wikipedia article.

To get a better handle on this, let's consider some more examples.

`levenshtein_distance('kitten', 'smitten')` -> 2 (see below for steps)

1. `kitten` → `sitten` (`k` gets replaced by `s`)
2. `sitten` → `smitten` (insert between `s` and `i`)


`levenshtein_distance('beta', 'pedal')` -> 3 (see below for steps)

1. `beta` → `peta` (`b` gets replaced by `p`)
2. `peta` → `petal` (`l` gets inserted at the end)
3. `petal` → `pedal` (`t` gets replaced by `d`)


`levenshtein_distance('battle', 'bet')` -> 4 (see below for steps)

1. `battle` → `bettle` (`a` gets replaced by `e`)
2. `bettle` → `bettl` (the last `e` gets deleted)
3. `bettl` → `bett` (delete `l`)
4. `bett` → `bet` (delete `t`)


### Base Cases

Let's consider the base cases when one of the two strings is empty. What
should the Levenshtein distance be in this case?


### Recursive Step

Let's consider the different ways in which we can make the first character of
string `a` equal to the first character of string `b`. Here are the possible
cases.

* The first two characters are already equal
* Replace the first character of string _a_ with the first character of string _b_
* Insert the first character of string _b_ before the characters of string _a_
* Delete the first character of string _a_

For each of these steps we have to consider two things:

1. How much does this first step cost?
2. How much does it cost to make the rest of the two strings equal to each other

We'll work on this together as a class.


## Memoization

Last class, a lot of you had the chance to do this exercise:

> Write a function called choose that takes two integer, n and k, and returns
the number of ways to choose k items from a set of n (this is also known as
the number of [combinations](https://en.wikipedia.org/wiki/Combination) of k
items from a pool of n). Your solution should be implemented recursively using
[Pascal's rule.](https://en.wikipedia.org/wiki/Pascal%27s_rule)

Here is a sample solution:

``` python
def nchoosek(n, k):`
    """ returns the number of combinations of size k
    that can be made from n items.

    >>> nchoosek(5, 3)
    10
    >>> nchoosek(1, 1)
    1
    >>> nchoosek(4, 2)
    6
    """
    if k == 0:
        return 1
    if n == k:
        return 1
    return nchoosek(n - 1, k - 1) + nchoosek(n - 1, k)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
```

It passes all the unit tests!!! Hooray!

Unfortunately, this code is going to be quite slow. To get a sense of it, we
will draw a tree that shows the recursive pattern of the function.

In order to improve the speed of this code, we can make use of a pattern
called memoization. The basic idea is to transform a recursive implementation
of a function to make use of a cache (in this case a Python dictionary) that
remembers all previously computed values for the function. Here's is a
skeleton of a memoized recursive function (we are being a little fast and
loose with the mixing pseudo code and Python, but this should become clear
when we do a concrete example.

``` python
def recursive_function(input1, input2):
    if input1, input2 is a base case:
        return base case result
    if input1, input2 is in the list of already computed answers
        return precomputed answer
    return recursive step on a smaller version of input1, input2
```

Next, try to modify our function `nchoosek` to use memoization.

{{ comment }}
The call graphs of the memoized nchoosek and Levenshtein functions are
[here](https://github.com//sd16spring/ClassNotes/blob/master/Call%20Graphs%202.ipynb).
{{ endcomment }}
