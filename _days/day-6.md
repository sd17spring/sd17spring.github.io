---
title: Day 6
date: 2017-02-02 00:00:00 -05:00
activity_date: 2017-02-02
description: Turtles and Toolboxes
---

## Today

* The original Turtle before TurtleWorld
* Completing the Gene Finder Mini-Project
* Preparing to tackle toolboxes (on your own time)

## For Next Time

* Reading journal, Think Python 5.8-5.14, 6.5-6.11

## Turtle Tales

As part of your work in the reading journals, you have now had opportunities to tell a graphical turtle named Bob to move around in a graphical window. To understand where TurtleWorld() drew its inspiration, see [the turtle's ancestry](http://el.media.mit.edu/logo-foundation/what_is_logo/logo_primer.html).

One of the reasons that you are beginning to work with turtles is because they have been helpful for visualizing recursion (which is a topic we will cover in the next class session).

See this example of turtle-flavored recursion used in one of the interactivepython.org lessons:

``` python
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)

drawSpiral(myTurtle, 100)
myWin.exitonclick()
```

## Toolbox Time

There is a chance that you will finish your Gene Finder Mini-Project before it is officially due. You can use the time that you have before Mini-Project 2 is kicked off on Monday to explore the Toolbox aspect of the class. Based on what you have done so far, you can start working on some of the Toolboxes listed (while others require some concepts we will be introducing soon).

[Toolboxes page]({% link _pages/toolboxes.md %})
