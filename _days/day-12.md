---
title: Day 12
date: 2017-02-27 00:00:00 -05:00
activity_date: 2017-02-27
description: Model-View-Controller
---

### Model-View-Controller

Model-View-Controller is what is known as a [software design
pattern](https://en.wikipedia.org/wiki/Software_design_pattern).


> In [software engineering](https://en.wikipedia.org/wiki/Software_engineering), a **[design
pattern](https://en.wikipedia.org/wiki/Design_pattern "Design pattern")**  is
a general reusable solution to a commonly occurring problem within a given
context in [software design](https://en.wikipedia.org/wiki/Software_design). A design pattern is not a finished design that can be
transformed directly into [source](https://en.wikipedia.org/wiki/Source_code) or [machine](https://en.wikipedia.org/wiki/Machine_code) code. It is a description or template for how to solve a
problem that can be used in many different situations. Patterns are formalized
[best practices](https://en.wikipedia.org/wiki/Best_practice)
that the programmer can use to solve common problems when designing an
application or system.
>
> \-- Wikipedia article on Software Design Pattern

The Model-View-Controller design pattern (or MVC for short) is an extremely
useful design pattern for a number of applications. The most common places
that it shows up are graphical user interfaces and web applications. Most
importantly it is ideally suited to the projects that you all will be doing
for this mini-project. Here is a figure that shows the basic principles of the
MVC design pattern.

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/500px-MVC-Process.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/500px-MVC-Process.svg.png)

> * A _controller_ can send commands to the model to update the model's state
(e.g. editing a document). It can also send commands to its associated view to
change the view's presentation of the model (e.g. by scrolling through a
document).
>
> * A _model_ stores data that is retrieved according to commands from the
controller and displayed in the view.
>
> * A _view_ generates an output presentation to the user based on changes in
the model.
>
> \-- Wikipedia article on Software Design Pattern

This decomposition has a number of extremely nice properties. At the highest
level, the pattern allows for the writing of loosely coupled and highly
modular code. This allows various components to be swapped out with minimal
changes to the overall program. However, in order to see the full power of
MVC, it helps to go through one cycle of using it to solve a problem.

## Links

* [Wikipedia: Model-View-Controller](https://en.wikipedia.org/wiki/Model–view–controller)
* [Coding Horror: Understanding Model-View-Controller](https://blog.codinghorror.com/understanding-model-view-controller/)
* Advanced: MVC is a design pattern – a pattern that relates multiple classes.
    * Design patterns: [Wikipedia](http://www.oodesign.com/); [online catalog](http://www.oodesign.com/); [book](https://en.wikipedia.org/wiki/Design_Patterns); [inspiration](https://en.wikipedia.org/wiki/Pattern_(architecture))

## Brick Breaker

We have spent some time getting you familiar with objects in Python. We now need to explore why they are powerful. We will build up an example project together that is in the video game space – so that you can be in a position to transfer your learning to your homework assignment.

Let's see how far we can get into making a game similar to a classic – **Breakout** for the Atari 2600.

<iframe width="560" height="315" src="https://www.youtube.com/embed/JRAPnuwnpRs" frameborder="0" allowfullscreen></iframe>

We will utilize the [Model-View-Controller](http://en.wikipedia.org/wiki/Model–view–controller) design method, to give everyone a concrete example of the kind of architecture we expect you to produce in your homework.

The code will rely upon pygame so make sure that it is installed – see the instructions for [Mini-Project 4]({% link _assignments/mini-project-4-interactive-visualization.md %}#pygame) to get Pygame set up if you have not done so.

[brickbreaker-sp17.py](/files/activities/mvc/brickbreaker-sp17.py)

## Bouncy Ball

I will start with a file [`bounce.py`](/files/activities/mvc/bounce.py), and refactor it to use MVC.

It will end going throught something like the following progression:

* [bounce_mv.py](/files/activities/mvc/bounce_mv.py)
* [bounce_mvc.py](/files/activities/mvc/bounce_mvc.py)
* [bounce_mvc_2.py](/files/activities/mvc/bounce_mvc_2.py)

**Optional exercise**

Refactor [spin.py](/files/activities/mvc/spin.py) to use MVC.
Optional optional: add some flair to it.
