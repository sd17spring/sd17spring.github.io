---
activity_date: 2017-02-21
date: 2017-02-21
description: Text mining mini-project work and making classes
published: false
title: Day 10
---

## Today

* Classes - defining your own Python types
* Studio work time on the text mini mini-project

## For Next Time

* Reading journal
* Mini Project 3 due Thursday
* Optional: Submit 1-2 slides with results from your MP3 (described below)
* [Choose MP4 topic and partner]({% link _assignments/mini-project-4-interactive-visualization.md %}#getting-started) (before the end of Thursday's class)
* [MP4 project proposal]({% link _assignments/mini-project-4-interactive-visualization.md %}#project-proposal)


## In-Class Exercise: Geometry Classes

In this exercise, you will define methods for `Line` and `Rect` geometry
classes.

Save the file
[geometry.py](https://github.com/sd17spring/sd17spring.github.io/blob/master/files/activities/day-10/geometry.py)
to your file system, and modify it so that the doctests pass:

``` bash
python geometry.py
```

In order to run the doctests for a _single method, comment out
`doctest.testmod` and uncomment `doctest.run_docstringexamples` at the end of
the file:

``` python
doctest.testmod()
# doctest.run_docstringexamples(Line.__repr_, globals())
```
→
``` python
# doctest.testmod()
doctest.rundocstring_examples(Line._repr_, globals())
```

You can use the `Point` class from the reading, but you are not required to.

Two of the methods in this file, `Line.intersection` and `Rect.intersection`,
have their doc tests commented out. (Yes, they're commented out within a
comment.) You don't need to implement these. They're the subject of the third _Going Beyond_ exercise, below.

Think about:

1. A rectangle conceptually has _left_, _right_, _top_, and _bottom_ coordinates, as well as _width_ and _height_. How many of these do you need to store, and how many can be calculated? Which ones will make the implementation of the class methods simpler?
2. Line's initialization method takes two _x_ coordinates in either order (x0 &lt; x1, or x1 &lt; x0). Is there work you could do when you initialize the object, that would make it easier to implement the methods.
3. What are the pros and cons of adding a `Square` class?

[You're encouraged to think about the first two questions before or while you
perform this exercise. Think about the last question afterwards, if you have
time.]_ If you have time_, you can extend your work in any of the following
directions. Any of these can be done independently of the others.

### Going Beyond 1: Duck Typing Skills emphasized: object-oriented programming (classes); polymorphism (“duck typing”).

Save the file
[geometry_beyond_1.py](https://raw.githubusercontent.com/{{site.course.github_owner}}/ClassNotes/master/geometry_beyond_1.py),
implement the methods of the `Circle` class, and implement the function `stochastic_area`.
`stochastic_area` should work on either a Rect or a Circle.

Some things to think about:

* How close is stochastic_area's return value to Rect and Circle's area methods?
* What needs to be true of a class for stochastic_area to work on it?
* Are there additional classes that would be simple to implement, that you could apply stochastic_area to?
* When would you use stochastic_area instead of just `area`?

### Going Beyond 2: PyGame – Skill emphasized: computer graphics

Save the file
[geometry_beyond_2.py](https://raw.githubusercontent.com/{{site.course.github_owner}}/ClassNotes/master/geometry_beyond_2.py),
and modify the implementation of `draw_shapes` to attend to its argument (a
list of shapes).


### Going Beyond 3: Geometry algorithms

_Skill emphasized: computation geometry and computer algorithms._

You guessed it: un-comment the test cases in `Line.intersection` and
`Rect.intersection` and make them pass.

Think about:

* What should `Line.intersection` and `Rect.intersection` do when the two lines or rectangles don't intersect? Can you think of several answers? – what are their pro and cons?


### Going Beyond 4: Test Case Design

_Skill emphasized: software engineering._

Think about the mistakes a non-malicious programmer could make while
implementing these methods. Do the test cases detect these mistakes? What
would you add?

You may do this exercise by drawing lines, squares, and points on a piece of
paper, instead of covering coordinates to numbers.


## Submitting Text mining-project slides

If you'd like to share what you discovered/created as part of your text mining
project, please add ~1-2 slides to the appropriate class presentation
[[SoftDes Spring 2017 spring 2017 MP3 examples]](https://docs.google.com/presentation/d/1fybuwS68fdgCHrhOMcpbDzZOfDhzUJsEiOQ_24pUQHI/edit?usp=sharing)
We'll spend time in Thursday's class presenting your
results.

Professionalism is important in public presentations, so please use the "would
I be happy for my parents to read this in the newspaper" test when uploading
content. Humor is great; abusive language or disparaging groups of people is
firmly not acceptable.
