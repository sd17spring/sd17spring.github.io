---
title: Day 21
date: 2017-04-06 00:00:00 -04:00
activity_date: 2017-04-06
description: Project website/README, organizing large projects, code review demo
---

## Today

* README files
* Project websites
* Organizing large Python projects
* Code review demo
* Code review signup
* Mini-Project 5 tips

## For Next Time

* Start your project website and link to it from your GitHub repository
* Create/update your README file
* Ensure your code so far is checked in and ready for the (encouraged, yet optional) code review on Monday
* No reading journal assigned


## README files

Every project should have a README file explaining what it does, how to run
it, etc. Today in class we'll discuss what makes a good README file. The
guidelines that we generated together formed the basis of the [README
rubric]({% link _assignments/final-project/readme-rubric.md %}) for the
final project.


## Project websites

Each team will be creating a [project website]({% link _assignments/final-project.md %}#project-website) as part of the final
project. Today in class, we'll help you get started building your website
using [GitHub pages](https://pages.github.com/).

For inspiration, you can look at some of the [2016 project websites]({% link _assignments/final-project/2016-project-websites.md %}).

{% comment %}
The example Rocco developed in class can be found at
<http://rdiverdi.github.io/GitExample> and
<https://github.com/rdiverdi/GitExample>
{% endcomment %}

For creating a single-page website with multiple sections, you can use the
GitHub automatic page creator/editor. If you'd like to expand to multiple
pages things get trickier. Fortunately Spring 2016 NINJAs Patrick and Franton have written
[an example and guide to multi-page GitHub websites using
Markdown](http://phuston.github.io/patrickandfrantonarethebestninjas/howto).

## Organizing large Python projects

As your Python projects grow too large to comfortably fit in a single file,
it's helpful to introduce more organizational structure. In Python, this is
done via modules

**Read:**  [Python modules](https://docs.python.org/3/tutorial/modules.html).

We've created [an example](https://github.com//{{site.course.github_owner}}/python-modules) where
we start from a single-file program and gradually add organization. You can
trace the evolution of the project by following along in the [git
history](https://github.com//{{site.course.github_owner}}/python-modules/commits/master).

Looking at project history on GitHub is nice, but you should also be able to
do the same thing from the command line.

1. Read about [Viewing Old Commits](https://www.atlassian.com/git/tutorials/viewing-old-commits/) in git.
2. Clone the project to your computer.
3. Explore around the project history.  Commands you should definitely practice include `git log`, `git diff`, `git history`, `git whatchanged`, and `git checkout`

**Exercise:**  (recommendation) As part of your Mini-Project 5 work, refactor and organize code from a previous submission (project or toolbox) into separate classes, files, and modules.
