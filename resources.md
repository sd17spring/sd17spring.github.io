---
date: '2016-12-29T18:26:01'
description: ''
title: Resources
layout: single
permalink: /resources/
---

{% include toc %}

This page lists web sites, PDF documents, Piazza posts, IPython notebooks, and
Python packages that have been mentioned during the course.

It's not an attempt to list everything related to each of those topics; just
to collect those resources that have already been mentioned into one place.

## Linux (Ubuntu)

* [Get Set (this site): Install and Configure Ubuntu](/assignments/setup-your-environment#step-1-install-and-configure-ubuntu)
* [Linux at Olin (downloadable PDF)](/assignments/setup-your-environment/linux.pdf)
* [Spring 2014 NINJA tutorial: Wireless issues on Ubuntu](https://docs.google.com/document/d/1uRRyjQhWyoffL_FNpRHNn8geblh9h0mfvAjjZ0fOtRc/edit)

## Classroom collaboration tools

{% if site.course.flootbits_url %}* [Floobits]({{site.course.flootbits_url}}) – code sharing{% endif %}
* [Piazza]({{site.course.piazza_url}}) – message board
* [Github](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Day5_Iteration.ipynb) – assignments
* [Github reading journal assignments](https://github.com//{{site.course.github_owner}}/ReadingJournal)

## Git

* [Git Help (this site)](/github-help) – contains links to additional resources
* [Pro Git](https://github.com/AllenDowney/amgit/tree/master/en) (Allen Downey's modification)
{% if site.course.piazza_url == 'https://piazza.com/olin/spring2016/engr2510' %}
* Piazza post: [Github merge conflicts and other issues](https://piazza.com/class/ijkborva8jk70v?cid=57)
* Piazza post: [Teaching git to ignore files](https://piazza.com/class/ijkborva8jk70v?cid=97)
{% endif %}
{% if site.course.github_url == 'sd17spring' %}
* [SoftDes16 Github page](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Day5_Iteration.ipynb)
{% endif %}
* [Spring 2014 NINJA tutorial: Github Help](https://docs.google.com/document/d/12mYDk2Bto-8a4LEq3tL9gvNO_8uehsyaV5WMg2-WNj4/edit)
* [Spring 2014 NINJA tutorial: Introduction to Version Control](https://docs.google.com/presentation/d/15UsxsUBIDA78iplWfKsX0yZAoYIf5ofpEr7PRUE2Y28/edit#slide=id.p)
* [Spring 2014 NINJA tutorial: Pushing to your Github repository](https://docs.google.com/document/d/1faRvcK33bIetPkgBH5Vw3Vlz8vl6jdPFKvtowT6Q1xw/edit)

## Python

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) – the class text
* [Python 3.5 Documentation](https://docs.python.org/3.5/)
* [Python 3.5 Standard Library](https://docs.python.org/3.5/library/index.html)
* Python Style
* [Spring 2014 NINJA tutorial: Python exercises](https://docs.google.com/document/d/1k-JU9cPokJ58ur4ubpbhLAxC26aAx9bCUcianobBLFE/edit)
* [Lambda functions](http://www.secnetix.de/%7Eolli/Python/lambda_functions.hawk)
{% if site.course.piazza_url == 'https://piazza.com/olin/spring2016/engr2510' %}
* Piazza post: [Python performance strategies](https://piazza.com/class/ijkborva8jk70v?cid=105) ([notebook](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Python%20Performance%20Strategies.ipynb))
* Piazza post: [Testing functions that call random](https://piazza.com/class/ijkborva8jk70v?cid=103)
{% endif %}

### Python Libraries

This section lists libraries that are somewhat general-purpose: they're
introduced in a particular assignment or project toolbox, but could be useful
in other projects too.

* [Numpy](http://www.numpy.org) scientific computing (including arrays)
* [Pattern](http://www.clips.ua.ac.be/pattern) data mining, natural language processing, and more
* [OpenCV-Python](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_ tutorials.html) image processing and computer vision
* [Pillow](http://python-pillow.org) image processing
* [Pygame](http://www.pygame.org/hifi.html) realtime image display
* [scikit-learn](http://scikit-learn.org/stable/) machine learning
* [Matplotlib](http://matplotlib.org) graphing and plotting ([Jupiter tutorial](http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)). Also see [Bokeh](http://bokeh.pydata.org/en/latest/) and [Seaboard](http://stanford.edu/~mwaskom/software/seaborn/).

### IPython Notebooks

{% if site.course.github_url == 'sd17spring' %}
* [Iteration strategies](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Day5_Iteration.ipynb)
* [Performance strategies](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Python%20Performance%20Strategies.ipynb)
* [Drawing call graphs](https://github.com//{{site.course.github_owner}}/ClassNotes/blob/master/Call%20Graphs.ipynb)
{% endif %}

## Atom Text Editor

* [Atom documentation](https://atom.io/docs)
* [Atom flight manual](http://flight-manual.atom.io)
