---
date: '2016-04-04'
description: 'Debugging and profiling'
title: Day 19
---

**Today**

* Python debugger
* Code profiling in Python

### Getting to "Good Code" (TM)

For today's purposes, we'll define "good code" to be correct and fast. There
are other equally important considerations, such as good documentation and
organization, but these are harder to measure quantitatively.


**Is the code correct?**

If your code doesn't do what it is supposed to, then nothing else matters.
We've discussed and practiced strategies for ensuring this, such as unit
testing. In situations when getting to "correct" proves difficult, it may be
helpful to employ more advance debugging strategies.


**Is the code fast enough?**

If the code is doing what it should, the next question is whether it runs fast
enough. There are several tools we can use to probe execution performance. The
answer to this question depends on context, but if the answer is "no" then we
need to dig deeper.


**Why not?**

For code with performance issues, it is important to understand precisely what
makes it slow. For this, we often turn to profiling to pinpoint bottlenecks in
execution so that they can be fixed.

"Python is slow", "my CPU is slow", "I need more RAM", and similar answers are
never acceptable without specific evidence. Faster hardware can sometimes
help, but buying a shiny new machine is not the solution when a poor algorithm
is the core of the problem (and much cheaper to fix).


## Something's not correct... Tools for debugging

One of the methods of debugging we've used so far in this class is print
statement debugging. Print statement debugging is fantastic, however, there
are some shortcomings. Take a minute and at your table discuss some less-than-
ideal aspects of print statement debugging.

Another form of debugging is to use a tool that allows interactive engagement
with either a crashed or running program. The Python DeBugger (pdb) can be
used in roughly these two modes: postmortem analysis and live execution. Today
we will only be covering the usage in live execution mode (for a discussion of
using pdb for postmortem analysis check out the [pdb
documentation](https://docs.python.org/2/library/pdb.html) under "analyzing a
crashed program").

There are a variety of approaches to using PDB in this capacity. One method is
to add the **pdb.set_trace**  command to your program to tell the debugger to
pause execution at a particular location and enter interactive mode.

``` python
import pdb

def factorial(n):
 """ Computes the factorial of the non-negative input integer n """
 return_val = 1
 pdb.set_ trace()
 for i in range(n):
 return_val *= i
 return return_val

if_ _name_ _ == '_ _main_ _':
 print factorial(5)
```

Let's debug this one together.

Some important commands for pdb:

  * c - continue until next set_trace or breakpoint
  * n - next line in current function
  * s - step until first opportunity to stop (either in current function or a called function)
  * l - source code listing
  * a - arguments of function
  * d - down a level in the stack diagram
  * u - up a level in the stack diagram
  * p - print the value of an expression
  * w - where are you in the stack

For more practice, pull the latest changes from the `ClassNotes` repo.

`git pull upstream master`

Navigate to the directory `ClassNotes/``pdb_practice` and try to use the
Python debugger to debug each of the four Python programs. The goal is not
only to find the bugs (you can probably do that without the debugger), but
instead to practice using the debugger as one of the debugging tools in your
arsenal.


### WinPDB

WinPDB is an advanced Python debugger. One nice thing that it has is a
graphical user-interface that makes the process of debugging more scaffolded.
You can install winpdb by running: `sudo apt-get install winpdb`

Alternate installation from source: First, download the source
[here](https://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/winpdb/winpdb-1.4.8.tar.gz). Next, extract it, cd
to the extracted folder, and run `sudo python setup.py install -f`.

Once you have installed winpdb, try it out by running the following command:

`$ winpdb ~/ClassNotes/pdb_ practice/debugging_exercise_ 1.py`


### Fast enough? Tools for benchmarking execution

Performance is always relative - 30 seconds is great for analyzing a huge
research data set and terrible for processing a credit card sale. It is also
machine-specific, though relative performance trends are often constant across
machines.

There are several tools available for benchmarking program execution to try to
scientifically answer the question of how fast your program runs.

1) You can time how long a Linux command takes using the [time
utility](http://manpages.ubuntu.com/manpages/trusty/man1/date.1.html):

``` bash
$ time python gene_finder.py
real 0m13.334s
user 0m12.493s
sys 0m0.012s
```

2) To measure at a finer granularity, you can use [Python time
module](https://docs.python.org/2/library/time.html) to measure the time
before and after a function call as we did in the [Day 17](/in-class-
exercises/day-17) exercises.

3) You may have noticed some variability in your results on the Day 17
exercises. To run many experimental trials of a small snippet of code, you can
use the [Python timeit module](https://docs.python.org/2/library/timeit.html).
`timeit` takes a string representing the code you want to time and runs it
repeatedly to get an average result.

`timeit` can be run from the command line (like the Linux time utility):

``` bash
$ python -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 3: 33.4 usec per loop
```

It can also be run from within a Python program (there is an example at
<https://github.com//{{site.course.github_owner}})/ClassNotes> in the profiling folder).

`timeit` is best used for testing very small sections of code (e.g. a single
line). For understanding larger programs, you should consider code profiling.


**Exercise**

Use `timeit` to compare `reverse_complement_ 1` and `reverse_complement_ 2` from
Day 17. Do the results match your analytical understanding?


## Why is this slow? Tools for profiling

Once you've determined that your program is too slow for your requirements,
it's time to figure out precisely why.

For this, we can use the [Python profile and cProfile
modules](https://docs.python.org/2/library/profile.html). For our purposes
these are equivalent, so we will use the faster cProfile module.

``` bash
$ python -m cProfile gene_finder.py
 35206053 function calls (35205065 primitive calls) in 18.516 seconds

 Ordered by: standard name

 ncalls tottime percall cumtime percall filename:lineno(function)
 1 0.000 0.000 0.000 0.000 <string>:1(<module>)
 1 0.000 0.000 0.000 0.000 <string>:1(ArgInfo)
 1 0.000 0.000 0.000 0.000 <string>:1(ArgSpec)
...
```

The profile listing that results shows lots of useful information about your
program execution. For each function (and builtin function) in the program,
cProfile lists:

* **filename:lineno(function)** : the function being profiled
* **ncalls** : number of times it was called
* **tottime** : the total time spent in that function
* **percall** : tottime/ncalls
* **cumtime** : time spent in the function, including subfunction calls

You can sort by any of these columns by providing a -s [sort_order] flag
(default is function name). You can also dump the profiling results to a data
file, so that you can run the program once and study the results at your
leisure. Full details are at the [profile
documentation.](https://docs.python.org/2/library/profile.html)


**Exercise**

I've started writing a palindromic phrase generator, but I'm struggling with
performance issues. I've started by searching for "mirror pairs" - words that
are valid both forward and backward, like "tuba" and "abut". Unfortunately, I
can't search my entire word list in a reasonable amount of time - checking
just the first 100 words takes about 15 seconds:

``` bash
$ time python mirror_pairs.py
['aa', 'aba']

real 0m14.620s
user 0m10.866s
sys 0m0.042s
```

Download the starter code from <https://github.com//{{site.course.github_owner}})/ClassNotes>, in
the profiling folder. Use cProfile to determine the bottleneck(s) in execution
and fix them.

Hint: It may be useful to revisit [Think Python Appendix
B](http://greenteapress.com/thinkpython/html/thinkpython022.html), especially
B.3 and B.4. You do not need to keep the architecture/functional organization
of the original code if it is slowing things down.


**Exercise**

Go back and profile your code for GeneFinder (and the other mini projects).
Where does your program spend most of its time? Are there bottlenecks you can
improve?

If you're looking for other interesting code to profile, check out Oliver's
excellent range of implementations with different performance characteristics:

[Gene Finder](https://piazza.com/class/ijkborva8jk70v?cid=122)
[Computation Art](https://piazza.com/class/ijkborva8jk70v?cid=131)
