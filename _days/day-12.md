---
date: '2017-02-23'
description: Model-View-Controller
published: false
title: Day 12
---

**Today**

* Model-view-controller
* In-class game implementation
* Review project proposals

**For Next Time**

* Reading journal day 12 (ThinkPython Chapter 18)
* Mid-project checkin with a NINJA due this Thursday (remember there is no class that day)

### Model-View-Controller

Model-View-Controller is what is known as a [software design
pattern](https://en.wikipedia.org/wiki/Software_design_ pattern).


> In [software engineering](https://en.wikipedia.org/wiki/Software_engineering
"Software engineering" ), a **[design
pattern](https://en.wikipedia.org/wiki/Design_pattern "Design pattern" )**  is
a general reusable solution to a commonly occurring problem within a given
context in [software design](https://en.wikipedia.org/wiki/Software_design
"Software design" ). A design pattern is not a finished design that can be
transformed directly into [source](https://en.wikipedia.org/wiki/Source_ code
"Source code" ) or [machine](https://en.wikipedia.org/wiki/Machine_code
"Machine code" ) code. It is a description or template for how to solve a
problem that can be used in many different situations. Patterns are formalized
[best practices](https://en.wikipedia.org/wiki/Best_ practice "Best practice" )
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

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-
Process.svg/500px-MVC-
Process.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-
Process.svg/500px-MVC-Process.svg.png)

> * A _controller_  can send commands to the model to update the model's state
(e.g. editing a document). It can also send commands to its associated view to
change the view's presentation of the model (e.g. by scrolling through a
document).
>
> * A _model_  stores data that is retrieved according to commands from the
controller and displayed in the view.
>
> * A _view_  generates an output presentation to the user based on changes in
the model.
>
> \-- Wikipedia article on Software Design Pattern

This decomposition has a number of extremely nice properties. At the highest
level, the pattern allows for the writing of loosely coupled and highly
modular code. This allows various components to be swapped out with minimal
changes to the overall program. However, in order to see the full power of
MVC, it helps to go through one cycle of using it to solve a problem.


### Brick Breaker

Let's make a game!

Let's start out by listing out the basic classes of our game. The easiest
place to start is with the model and the view. We'll start there and do the
controller last.

It will help to have a [pygame cheat
sheet](http://inventwithpython.com/blogstatic/pygamecheatsheet.png?27f655)
handy so that you can better follow along with the tutorial.

