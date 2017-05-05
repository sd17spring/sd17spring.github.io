## Getting to "Good Code" (TM)

For today's purposes, we'll define "good code" to be correct and fast. There
are other equally important considerations, such as good documentation and
organization, but these are harder to measure quantitatively.

### Is the code correct?

If your code doesn't do what it is supposed to, then nothing else matters.
We've discussed and practiced strategies for ensuring this, such as unit
testing. In situations when getting to "correct" proves difficult, it may be
helpful to employ more advance debugging strategies.

### Is the code fast enough?

If the code is doing what it should, the next question is whether it runs fast
enough. There are several tools we can use to probe execution performance. The
answer to this question depends on context, but if the answer is "no" then we
need to dig deeper.

### Why not?

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
documentation](https://docs.python.org/3/library/pdb.html) under "analyzing a
crashed program").

There are a variety of approaches to using PDB in this capacity. One method is
to add the `pdb.set_trace` command to your program to tell the debugger to
pause execution at a particular location and enter interactive mode.

```python
import pdb

def factorial(n):
 """Compute the factorial of the non-negative input integer n."""
 return_val = 1
 pdb.set_trace()
 for i in range(n):
 return_val *= i
 return return_val

if __name__ == '__main__':
 print(factorial(5))
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

Navigate to the directory `ClassNotes/pdb_practice` and try to use the
Python debugger to debug each of the four Python programs. The goal is not
only to find the bugs (you can probably do that without the debugger), but
instead to practice using the debugger as one of the debugging tools in your
arsenal.

### WinPDB

WinPDB is an advanced Python debugger. One nice thing that it has is a
graphical user-interface that makes the process of debugging more scaffolded.
You can install winpdb by running: `sudo apt-get install winpdb`

Alternate installation from source: First, download the source
[here](https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/winpdb/winpdb-1.4.8.tar.gz). Next, extract it, cd
to the extracted folder, and run `sudo python setup.py install -f`.

Once you have installed winpdb, try it out by running the following command:

`$ winpdb ~/ClassNotes/pdb_practice/debugging_exercise_1.py`

## Fast enough? Tools for benchmarking execution

Performance is always relative - 30 seconds is great for analyzing a huge
research data set and terrible for processing a credit card sale. It is also
machine-specific, though relative performance trends are often constant across
machines.

There are several tools available for benchmarking program execution to try to
scientifically answer the question of how fast your program runs.

1) You can time how long a Linux command takes using the [time
utility](http://manpages.ubuntu.com/manpages/trusty/man1/date.1.html):

```bash
$ time python gene_finder.py
real 0m13.334s
user 0m12.493s
sys 0m0.012s
```

2) To measure at a finer granularity, you can use [Python time
module](https://docs.python.org/3/library/time.html) to measure the time
before and after a function call as we did in the [Day 17](/in-class-exercises/day-17) exercises.

3) You may have noticed some variability in your results on the Day 17
exercises. To run many experimental trials of a small snippet of code, you can
use the [Python timeit module](https://docs.python.org/3/library/timeit.html).
`timeit` takes a string representing the code you want to time and runs it
repeatedly to get an average result.

`timeit` can be run from the command line (like the Linux time utility):

```bash
$ python3 -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 3: 33.4 usec per loop
```

It can also be run from within a Python program (there is an example at
<https://github.com//{{site.data.course.github.owner_name}}/ClassNotes> in the profiling folder).

`timeit` is best used for testing very small sections of code (e.g. a single
line). For understanding larger programs, you should consider code profiling.

### Exercise

Use `timeit` to compare `reverse_complement_1` and `reverse_complement_2` from
Day 17. Do the results match your analytical understanding?

* open time to work on projects
