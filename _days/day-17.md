---
title: Day 17
date: 2017-03-23 00:00:00 -04:00
published: false
activity_date: 2017-03-26 20:00:00 -04:00
description: Analysis of algorithms
---

## Today

* Analysis of algorithms

All of the planned class activities will be done with the people at your
table. The optimal number is probably four.

## Reading Journal Debrief

At your table, discuss the following questions:

1. What are some of the challenges in comparing the efficiency of two algorithms?
2. How does order of growth analysis address these challenges?
3. In what situations might order of growth analysis be misleading (or at least tell an incomplete story)?
4. Review your answers to Appendix B Problem 1 (from the reading journal). If there is confusion about one of the answers, take some time to discuss it at your table in more detail (or use the whiteboard).
5. If any questions come up that you'd like to raise with the whole class, there will be some time to do so following your small group discussions.

## Practice with Order of Growth

Suppose we are given two python functions `do_procedure_f1` and
`do_procedure_f2`. Each function processes a list `L`  in some fashion
(what these programs do is unimportant for this exercise). We are told that
the order of growth of these procedures is:

* `do_procedure_f1`  is `O(n)` (where n is the length of the input list `L`)

* `do_procedure_f2`  is `O(1)` (where n is the length of the input list `L`)

What are the order of growths of the following computations?

``` python
def run_computation_1(L):
   do_procedure_f1(L)
   do_procedure_f2(L)
```

``` python
def run_computation_2(L):
   do_procedure_f1(L[0:5])
   do_procedure_f2(L)
```

``` python
def run_computation_3(L):
   for i in range(len(L)):
      do_procedure_f1(L)
```

``` python
def run_computation_4(L):
  for i in range(len(L)):
      do_procedure_f2(L)
```

``` python
def run_computation_5(L):
    if len(L) % 2 == 0:
        do_procedure_f1(L)
    else:
        do_procedure_f2(L)
```

``` python
def run_computation_6(L):
    if len(L) == 1:
        return 1
    else:
        do_procedure_f2(L)
        run_computation_6(L[0:len(L)/2])
```

### Order of Growth for Basic Python Operations

You have read Think Python Appendix B.1 and B.2. One of the most important
takeaways is the listing of the order of growth for various operations on
Python data structures. Here are some key points:

* Removing an element from the end of a list is constant time
* Adding an element to the end of the list is constant time (on average)
* Testing if an element is in a list is linear time, O(n)
* Looking up the value stored with a given key in a dictionary is constant time
* Looking up an element stored in a list at a particular location is constant time

#### Empirical Analysis of Order of Growth

Next, we will be doing an exercise to:

1. Practice the application of order of growth analysis to actual Python code
2. Explore how this analysis squares with an empirical analysis of the running time of Python code. The exercises for this portion of class can be found in the repository **https://github.com//{{site.course.github_owner}}/ClassNotes**  under **AnalysisOfAlgorithms.ipynb** .
