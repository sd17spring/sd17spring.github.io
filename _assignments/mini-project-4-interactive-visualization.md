---
date: 2017-01-20 07:38:35 -0500
description: ''
due_date: '2017-03-14'
title: 'Mini Project 4: Interactive Programming'
---

{% include toc %}

## Introduction

In the first three mini-projects you have written Python programs that do a
wide variety of things. You have written code to analyze data (mini-project 1
and 3), you have written code to make compelling visuals (mini-project 2), and
you have written code to automatically download information from the web
(mini-project 3). In this project we will be combining many of these threads.
The big idea of this project will be to move from static programs (ones that
are run, do some computations, and spit out a result) to interactive programs
(ones that allow the user to perform actions that change the state of the
program). The dance of user input and program response, will enable us to
write some very powerful software. Here are some ideas:

1. **Interactive data visualization:** as the amount of information available on the net explodes, there is an increasing need for tools that allow people to explore and understand the patterns in this data. During this exploratory stage, it is invaluable to have a tool that enables the user to rapidly explore various aspects and views of the data. Interactive visualization is an emerging and highly interdisciplinary field that straddles many disciplines including computer science, art, statistics, and even journalism. A potential SoftDes project in this space would be to write a program to download some data (or possibly acquire data in real-time, say from some sensor or a web API), display the data to the user in a clear and compelling format, and allow the user to dynamically explore various aspects of the data through a user interface.
2. **Video games:** video games are a clear example of an interactive program. A possible project in this space would be to develop a Python-based adaptation of your favorite game (classic arcade games or smartphone apps make ideal candidates). We encourage you to think broadly about using non-traditional input modalities (beyond keyboard and mouse). For instance, why not control a video game based on images captured by your laptop's webcam?

3. **Interactive art:**  a potential project in this space could be to create visuals or audio that is in some way responsive to the observer. The possibilities in this space are huge. One specific idea would be to create a computerized musical instrument that can be controlled through hand motions (where movements would be detected using computer vision).


### Deltas from Previous Projects

1. You will be working with a partner on this project (a single team of 3 will be permitted if a section has an odd number of students).
2. This project is more open-ended than previous projects. In the last mini-project you could choose the data and analysis tool that you wanted to explore. Here, not only do you have these choices, but you can also choose to make a very different thing (e.g. a video game versus an interactive data visualization).
3. You have more time to work on this project (2 weeks, versus 1 week for the last project).


### Computational Skills Emphasized

(some of these are only applicable to certain project topics)

* Object-oriented programming
* Event-driven programming
* Computer Graphics
* Physics Simulation
* Data visualization

### Teaming Logistics and Guidance

Teaming Logistics:

* You must work in a team of exactly two students (given an odd number of students we may have one team of three per section).
* Your partner must be in your section (no exceptions).
* Only one of you should fork the base repo for this assignment. The one that forks the repo should then add the other team member as a collaborator on GitHub for that repo.

Teaming Guidance:

* Do not thoughtlessly default to working with your friend.
* Make sure you and your potential partner are on the same page in terms of project topic.
* You should partner with someone that has roughly the same commitment level to the project. For instance, someone that is super gung-ho about making the most amazing SoftDes project evar should not partner with someone that is just looking to do the minimum.
* You should be mindful of differences in level of programming experience when selecting your partner. Teams that are very closely matched in terms of programming experience should be no problem. Teams that are not closely matched on this axis can also be quite effective. However, if you and your partner are not closely matched you will want to make sure that you are both vigilant about avoiding some common pitfalls that occur with this type of team. The two most common pitfalls are: the person with more experience gets frustrated with the other team member and does all the work, and the person with more experience writes all the code while the person with less experiences watches them.

## Recommended Libraries

You are welcome to use whatever library you'd like for this project, however,
there is a lot of benefit to sticking to the ones that we recommend. The best
reason for doing so are to ensure that we, the teaching team, can provide you
with as good support as possible as you use the library to complete the
project. If you pick a nonstandard library that none of us have used before,
we will have a tough time helping you if you run into problems (although we
will certainly try!).

### Pygame

For 2-d drawing, collision detection, and simple physics in Python, **pygame**
is a fantastic choice. Perhaps the biggest strength of **pygame**  is that it
has many [great tutorials](http://pygame.org/wiki/tutorials) as well as sample
games to use as starting points (for example [arcade
games](http://www.pygame.org/tags/arcade), [puzzle
games](http://pygame.org/tags/puzzle), and [platform
games](http://pygame.org/tags/platformer)).

Even though it might seem like odd choice, we are recommending **pygame**  as
the default library for those that are doing interactive visualization
projects. There are fancier libraries out there, however, you can build some
very nice interactive visualizations on top of the basic 2d drawing and mouse
and keyboard event handling components in **pygame** . Further, using a fancy
library reduces the amount of object-oriented code that you have to write, and
in this assignment we want you to get a lot of practice writing your own
object-oriented code. Sticking with a simple framework like **pygame** will
support this learning goal nicely. A final advantage is that we will be doing
at least one lengthy example in class that uses **pygame. I** f you are using
**pygame**  for your data visualization project, you will get a lot more out of
this inclass activity.

To install **pygame**:

`$ sudo apt-get install python-pygame`

How to get started with **pygame**  (these do not have to be done in this
order):

* [if making a game] Go through the PyMan tutorials ([part 1](http://www.learningpython.com/2006/03/12/creating-a-game-in-python-using-pygame-part-one/), [part 2](http://www.learningpython.com/2006/03/19/creating-a-game-in-python-using-pygame-part-two-creating-a-level/), [part 3](http://www.learningpython.com/2006/04/16/creating-a-game-in-python-using-pygame-part-3-adding-the-bad-guys/)). It is shows how to implement a Pacman clone in pygame (don't worry about the pre-requisites section, you should already have the pre-requisites satisfied). The strength of the tutorial is that there is lots of explanation of each part of the code. Unfortunately, the HTML formatting for parts 2 and 3 seems to be messed up, but hopefully these are still useful (let us know if you find a workaround for this formatting issue).
* Read through the **pygame**  [documentation](http://www.pygame.org/docs/).
* Read through the other **pygame**  [tutorials](http://pygame.org/wiki/tutorials) if you find one that seems more aligned with the project you want to create.
* [if making a game] Make sure you understand the basics of collision detection in **pygame** . Collision detection is a surprisingly tricky thing to write on your own, so it is recommended to utilize **pygame** 's built-in features for this (see [this](http://www.pygame.org/docs/tut/SpriteIntro.html) page). If you need to do collision detection with something besides rectangles, you may have to either adapt pygame's collision detection or write your own collision detection routines.

### OpenCV

If you want to use an input modality other than keyboard and mouse, you may
find the computer vision library OpenCV useful. The idea here would be to
capture images from a camera (probably the webcam on your laptop) and use
those to control some aspect of your program. To get started check out the
SoftDes [project toolbox exercise on OpenCV]({% link _toolboxes/image-processing.md %}). Next, read through the [OpenCV Python
tutorials](http://docs.opencv.org/trunk/doc/py_tutorials/py_ tutorials.html)
and [API reference](http://docs.opencv.org/2.4.9/modules/refman.html)).

### To Implement, or not to Implement, that is the question!

There are some inherent tradeoffs in using someone else's whiz-bang library
and coding the functionality yourself. Here are some pros and cons:

* **Pro:**  using a library is faster and can let you do things in a short time that would be infeasible if you coded it yourself.
* **Pro:**  you can mashup different libraries to do amazing things.
* **Con:**  if you are shaky on your basic understand of Python you may not learn the basics if you are relying too heavily on others libraries.
* **Con:**  if you get too far down the path of using a library and it doesn't do something important that you need, you are in a tough spot.

It's up to you how heavily you want to utilize others libraries. All we ask is
that you make the decision intentionally and with consideration of these
tradeoffs.

## Project Ideas

### Interactive Data Visualization

The first thing you will need to do is to get some data. Here are some
sources:

1. **The 538:** Nate Silver's website on data-driven journalism. They have a [github repo](https://github.com/fivethirtyeight/data) with data they use in their articles!
2. National Survey of Family Growth: Allen has a lot of examples that uses this database. To get started fork Allen's [ThinkStats2 repository](https://github.com/AllenDowney/ThinkStats2).
3. [Data.gov](http://data.gov/): a massive repository of data provided by the U.S. government.
4. A [very comprehensive](https://github.com/caesar0301/awesome-public-datasets) listing of sources for open data.
5. IBM's [Big Data for Social Good Challenge](http://ibmhadoop.challengepost.com/details/data)
6. Make your own dataset using Pattern (you should know how to do this from the last project).
7. ??? (the possibilities are endless, e-mail us if you find an awesome trove of data that you think the class should know about post it to Piazza).

Once you have the data you'll want to think about how you might using
visualization and user input to explore the data. To get your creative juices
flowing here are some cool examples of data visualization:

We will show a bunch of these examples below, but check out [the full
listing](http://www.nytimes.com/newsgraphics/2013/12/30/year-in-interactive-storytelling/#dataviz) from the New York Times Year in Interactive
Storytelling. This link is for 2013, but other years are available.

_Exploring How People Talk in Different Parts of the U.S. (source: New York
Times Year in Interactive Storytelling 2013):_

![]({% link images/assignments/interactive-visualization/dialect-screenshot.png %}{:width="400px" height="363px"}

[Exploring movie trailers](http://www.nytimes.com/interactive/2013/02/19/movies/awardsseason/oscar-trailers.html)
_(source: New York Times Year in Interactive Storytelling 2013)_

_Examining Box Office Hits:_
![]({% link images/assignments/interactive-visualization/4.png %}{:width="400px" height="222px"}

_Where did my harddrive space go???_

![]({% link images/assignments/interactive-visualization/29.png %}{:width="304px" height="400px"}


_ Examining the Group Debates:_
![]({% link images/assignments/interactive-visualization/37.png %}{:width="400px" height="229px"}

_[Examining the impact of medicaid expansion (or lack thereof) state-by-state](http://www.nytimes.com/interactive/2013/10/02/us/uninsured-americans-map.html)_
_(source: New York Times Year in Interactive Storytelling 2013)_

_[Fourth down bot](http://www.nytimes.com/newsgraphics/2013/11/28/fourth-downs/):

![]({% link images/assignments/interactive-visualization/4th-down-bot.png %}{:width="400px" height="295px"}


### Arcade Games

If you decide to create a game, you should probably choose one that has
relatively simple physics. Depending on how ambitious you are, you might want
to stick to a game where all of the action is contained within a single
screen. Here are some examples:_ Missile Command:_
_ Pacman:_ _ Skyroads (considerably more complex than the others, but maybe a simple
version could be constructed):_
_ Asteroids (this version was created in another computing class. Check out
[this video](http://nifty.stanford.edu/2008/leyzberg-simon-asteroids/asteroids.avi) for the game in action place some cool
enhancements)._

![](http://nifty.stanford.edu/2008/leyzberg-simon-asteroids/game.jpg)


#### **Interactive Art**

There is a big universe out there. The pulsating music visualizer from the
last assignment was one example. Hooking up simple color tracking using OpenCV
to sound synthesis is also a nice one** ** (e.g. a musical instrument
controlled by movements). Check out the [Wikipedia
page](http://en.wikipedia.org/wiki/Interactive_art) for more ideas.


### Design Guidelines

The big computational content of this unit is object-oriented programming. As
a result, your code should make heavy use of objects! If you find that your
design does not have any classes or just one, then there is probably something
wrong. We will not be dictating / enforcing that you use any particular
object-oriented design pattern. However, we are going to be explicitly
scaffolding the use of a very powerful object-oriented design pattern called
[Model-View-
Controller](http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).
Here is a diagram (from Wikipedia) that shows the various components of Model-
View-Controller and how they interact:

![](http://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/1000px-MVC-Process.svg.png)

To make things concrete, let's think about how we might implement a Pacman
clone. Here are the classes and the functions that you might use to implement
your game:

* **Model:**  encodes the overall game state of the Pacman game (including level, position of pellets, position of Pacman and ghosts, etc.)
  * Provides an interface to the Controller to respond appropriately to user commands
  * Handles collisions between Pacman and ghosts as well as Pacman and small and large pellets
* **Pacman:**  represents the player's avatar in the game (a part of the model)
  * Provides an interface to respond to player actions as communicated by the controller (e.g. Pacman's next move)
* **Ghost:**  represents a ghost in the game (a part of the model)
* **Small pellet:**  represents a small pellet in the game (a part of the model)
* **Large pellet:**  represents a large pellet in the game (a part of the model)
* **Controller:**  handles commands from the user and manipulates the model appropriately
* **PyGameView:**  draws the game state encoded by the Model to a **pygame**  window

There are many ways to implement Model-View-Controller, so this is not the
only way to operationalize Model-View-Controller in the context of Pacman.
Remember, this is not the only way to structure your object-oriented design,
but we hope it will be helpful at least as a jumping off point.

## Project Deliverables

### Getting Started

You must find a teammate and decide on a project topic. You are required to
have your teammate selected (and hopefully a rough idea of what you will do
for the project) by noon on Saturday, February 27th. Use
[this]({{site.course.visualization_teaming_spreadsheet}}) Google spreadsheet to indicate who you are
working with. There is also a section where you can look for a teammate if you
don't have one already.

As part of filling out this spreadsheet, and starting the project, you should
fork and clone the [base repo](https://github.com//{{site.course.github_owner}}/InteractiveProgramming) for this project.
Remember, that you will want to have only one of your teammates fork the repo,
and then the other member should be added as a collaborator on GitHub for that
repo. Be sure to add a link to your repo to the shared Google spreadsheet.

There are three deliverables for this project.

### Project Proposal

This coming Monday you will be meeting with us to discuss your plans for this
project. You should come to next class with a PRINTED copy of a document that
describes the main idea of your project. We will only have 5 minutes to meet
with each team, so we ask that you come to the meeting without your laptop,
but with a printed version of your document. You should designate one of the
two team members to take notes. Here are the questions your document should
address:

  * What is the main idea of your project? What topics will you explore and what will you generate? What is your minimum viable product? What is a stretch goal?
  * What are your learning goals for this project?
  * What libraries are you planning to use? (if you don't know enough yet, please outline how you will decide this question during the beginning phase of the project).
  * What do you plan to accomplish by the mid-project check-in? (See below for some generic goals; edit to suit your particular project)
  * What do you view as the biggest risks to you being successful on this project?

This deliverable will not factor into your project grade. The purpose is
purely to allow us to help shape your project in useful directions.**
**

**Note: just because we will not have a chance to go over your project proposal until Monday 2/29 doesn't mean that you should wait until this meeting to actually start your project.**


### Mid-Project Checkin

We are requiring a mid-project check-in for this project. You must meet with a
NINJA by end-of-the-day Thursday March 3rd (we do not have class on that day).
The grading for this checkin will be 0% if you miss it or blow it off, 50% if
you have minimal work done before the checkin, and 100% if you have made a
sincere effort to get your project off the ground. The mid-project checkin
will comprise 20% of the final grade for this project.

Given that different teams' projects will be very different, there is no one
set of things that are appropriate for you to have done by the mid-project
checkin. We will have the opportunity to provide guidance around this when we
meet with you at the project proposal. However, here are a list of fairly
generic goals for the mid-project check-in:

* You should have good sense of the major classes that you will need to create for your project. A UML diagram (see ThinkPython) will be a useful thing to have as well.
* You should have a clear implementation plan. This includes how you will divide (or not divide) up the programming tasks among you and your partner.
* If you are planning to use a library that you read about, you should have verified that you can install it and that it can be used for the purpose that you want.
* You should have a good start on implementing some of the classes for your project.

#### Project Writeup and Reflection

Please prepare a short document (~1 page not including figures) with the
following sections:

**Project Overview** _[Maximum 100 words]_

Write a short abstract describing your project.


**Results**  _[~2-3 paragraphs + figures/examples]_

Present what you accomplished. This will be different for each project, but
screenshots are likely to be helpful.


**Implementation**  _[~2-3 paragraphs + UML diagram]_

Describe your implementation at a system architecture level. Include a UML
class diagram, and talk about the major components, algorithms, data
structures and how they fit together. You should also discuss at least one
design decision where you had to choose between multiple alternatives, and
explain why you made the choice you did.


**Reflection** _[~2 paragraphs]_

From a process point of view, what went well? What could you improve? Other
possible reflection topics: Was your project appropriately scoped? Did you
have a good plan for unit testing? How will you use what you learned going
forward? What do you wish you knew before you started that would have helped
you succeed?

Also discuss your team process in your reflection. How did you plan to divide
the work (e.g. split by class, always pair program together, etc.) and how did
it actually happen? Were there any issues that arose while working together,
and how did you address them? What would you do differently next time?


### Turning in your assignment

* Push your completed code to the "master" Git repository (depending on which team member's repository is being used to work on the project).
* Submit your Project Writeup/Reflection (1 per team, not 1 per person). This can be in the form of either:
  * a PDF document pushed to GitHub, or
  * a [project webpage](https://pages.github.com/) (if you choose this route, make sure there is a link to your webpage in your **README.md**  file in your GitHub repo)
* Open a pull request to the base InteractiveProgramming repo.

Your code must be adequately documented. This includes:

* Appropriate docstrings
* Comments inline in your functions
* README file that describes how to get your code to run

**Automatically generated documentation**

One way to ensure you have adequate docstrings is to generate documentation
from them. You can do this using
[pydoc](https://docs.python.org/2/library/pydoc.html):

`$ pydoc path/to/my_project.py`

This will open a help file based on your docstrings (use q to quit). Make sure
the help file would be useful to someone using your code, and feel free to
attach it to your writeup as an appendix.

If you want to generate truly beautiful documentation, check out
[Sphinx](http://sphinx-doc.org/) (the tool used to generate the [Python
documentation](https://docs.python.org/2/)). Certainly not required, but you
may want to use it in the future (think: final project)
