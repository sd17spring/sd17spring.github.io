---
title: Toolboxes
date: 2016-12-29 13:26:01 -05:00
permalink: toolboxes/
description: ''
layout: archive
---

Software Design and Python are wide worlds, and we'll only explore part of
them in class this semester. The goal of the Project Toolbox exercises is to
gain practice with a variety of interesting topics we won't talk about in
class. By completing them, you will develop a suite of skills that will allow
you to do great things on the final project and beyond.

The exercises are modeled after the way many practicing software developers
teach themselves as lifelong learners. In each, you'll:

  1. Read about a topic
  2. Try an example
  3. Extend it in ways that are interesting to you

The basic part of each exercise is intended to be relatively quick, taking an
hour or so. (If you find yourself taking significantly longer, be sure to ask
for help.) There are also lots of opportunities to take things further – many
of the topics are active research areas, and you could easily work on some of
them for a lifetime!

### Tips for success

* **Don't suffer in silence.** Many of these exercises require installing new packages, which can sometimes come with hiccups. If you're struggling with something, let us know about it on Piazza so we can fix it for you and everyone else.
* **Start early**. The project toolbox can be a great source of inspiration for your final project – but only if you try them in time.
* **Have fun** and follow your own learning goals.

## Toolboxes

{% assign toolboxes = site.toolboxes | sort: 'title' %}
{% for toolbox in toolboxes %}
* [{{ toolbox.title }}]({{ toolbox.url }}){% endfor %}

## Submitting exercises

Each Project Toolbox exercise has a description of the minimum required
deliverable. To submit your assignment, just push your code to GitHub and
submit a pull request to get checked off. For several of the exercises, you
may want to schedule a brief demo with a NINJA.

You will complete at least five Project Toolbox exercises. At least three must
be done before Spring Break (due by March 13th), and the remaining exercises
can be completed during the second week of the final project (due by March
28th).

If you get through the Project Toolbox exercises and you have a great idea for
a new one you'd like to create, get in touch with the teaching team!
