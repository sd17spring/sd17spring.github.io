---
title: Resources
date: 2017-02-22 10:10:00 -05:00
permalink: resources/
description: ''
---

{% include toc %}

This page lists web sites, PDF documents, Jupyter notebooks, and
Python packages that have been mentioned during the course.

It's not an attempt to list everything related to each of those topics; just
to collect those resources that have already been mentioned into one place.

## General

[Stack Overflow](http://stackoverflow.com) is a community of programmers, and a knowledge base of programming questions and answers. You can search it directly from its site; it also shows up in Google search results.

## Linux (Ubuntu)

* [Get Set (this site): Install and Configure Ubuntu]({% link _assignments/setup-your-environment.md %}#step-1-install-and-configure-ubuntu)
* [Linux at Olin (downloadable PDF)]({% link files/assignments/setup-your-environment/linux.pdf %})
* [Spring 2014 NINJA tutorial: Wireless issues on Ubuntu](https://docs.google.com/document/d/1uRRyjQhWyoffL_FNpRHNn8geblh9h0mfvAjjZ0fOtRc/edit)

## Git

See [Git Help]({% link _pages/git-help.md %}) on this site.

## Python

* [Think Python, by Allen Downey](http://greenteapress.com/wp/think-python-2e/) – the class text
* [Python 3.5 Documentation](https://docs.python.org/3.5/)
* [Python 3.5 Standard Library](https://docs.python.org/3.5/library/index.html)
* [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/), especially [Writing Great Python Code](http://docs.python-guide.org/en/latest/#writing-great-python-code)
* [Spring 2014 NINJA tutorial: Python exercises](https://docs.google.com/document/d/1k-JU9cPokJ58ur4ubpbhLAxC26aAx9bCUcianobBLFE/edit)
* [Lambda functions](http://www.secnetix.de/%7Eolli/Python/lambda_functions.hawk)
{% if site.data.course.urls.piazza == 'https://piazza.com/olin/spring2016/engr2510' %}
* Piazza post: [Python performance strategies](https://piazza.com/class/ijkborva8jk70v?cid=105) ([notebook](https://github.com//{{site.data.course.github.owner_name}}/ClassNotes/blob/master/Python%20Performance%20Strategies.ipynb))
* Piazza post: [Testing functions that call random](https://piazza.com/class/ijkborva8jk70v?cid=103)
{% endif %}

### Python Style Guides

* [PEP 8 – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
* [PEP 257 – Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
* [Google Style Guide](https://google.github.io/styleguide/pyguide.html)

### Python Libraries

This section lists libraries that are somewhat general-purpose: they're
introduced in a particular assignment or project toolbox, but could be useful
in other projects too.

Also see [Awesome-Python](https://awesome-python.com), a curated list of Python libraries.

#### Data Processing and Scientific Computing

* [Pandas](http://pandas.pydata.org) tables (like Excel) as a data type
* [NumPy](http://www.numpy.org) scientific computing (including arrays)
* [OpenCV-Python](https://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_tutorials.html) image processing and computer vision
* [Pillow](http://python-pillow.org) image processing
* [scikit-learn](http://scikit-learn.org/stable/) machine learning

#### Graphics and Interactivity

* [Pygame](http://www.pygame.org/hifi.html) real-time image display
    * [Pygame cheat sheet]({% link _pages/pygame-resources.md %}), written by sofdes ninjas
* [Matplotlib](http://matplotlib.org) graphing and plotting ([Jupiter tutorial](http://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)). Also see [Bokeh](http://bokeh.pydata.org/en/latest/) and [Seaboard](http://stanford.edu/~mwaskom/software/seaborn/).
* [Seaborn](http://seaborn.pydata.org) improves the appearance of Matplotlib graphs and adds additional features
* [Kivy](https://kivy.org/) for user interfaces

#### HTML and the Web

* [Flask](http://flask.pocoo.org) web applications (software that runs on a server and serves HTML pages to browsers)
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) parses HTML pages
* [Requests](http://docs.python-requests.org/en/latest/) retrieves HTML pages

{% if site.course.github_url == 'sd16spring' %}

### IPython Notebooks

* [Iteration strategies](https://github.com//{{site.data.course.github.owner_name}}/ClassNotes/blob/master/Day5_Iteration.ipynb)
* [Performance strategies](https://github.com//{{site.data.course.github.owner_name}}/ClassNotes/blob/master/Python%20Performance%20Strategies.ipynb)
* [Drawing call graphs](https://github.com//{{site.data.course.github.owner_name}}/ClassNotes/blob/master/Call%20Graphs.ipynb)
{% endif %}

## Text Editors

* [Atom](https://atom.io)
    * [Atom documentation](https://atom.io/docs)
    * [Atom flight manual](http://flight-manual.atom.io)
* [Sublime](https://www.sublimetext.com) is an alternative to Atom. It's faster for large files, but managing plugins is more difficult and it wants a commercial license.
* [Visual Studio Code](https://code.visualstudio.com) is the new kid on the block.
* [PyCharm](https://www.jetbrains.com/pycharm/) is an [Integrated Development Environment (IDE)](https://en.wikipedia.org/wiki/Integrated_development_environment).
It does more than the text editors, and is harder to learn.
