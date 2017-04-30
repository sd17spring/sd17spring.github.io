---
title: Day 25
date: 2017-04-30 19:21:00 -04:00
activity_date: 2017-04-27
description: Final deliverables
---

## Today

* Final project deliverables

## For Next Time

* SoftDes final project expo, {% if site.data.dates.final_expo %}{{ site.data.dates.final_expo | date: '%A, %b %-d, %H:%M %p' }}–{{ site.data.dates.final_expo_end | date: '%H:%M %p' }}{% else %}TBD{% endif %}

## Final project deliverables

We're at the end of the semester! You've done great work, implemented some
cool code, and worked together with your peers to help each other improve. The
remaining deliverables are intended for you to share that work with various
audiences.

### Website

_Due: end of day {{site.data.dates.final_website | date: '%A, %B %-d' }}_

_Final revision, incorporates instructor feedback, due_: end of day {{site.data.dates.final_website_feedback_addressed | date: '%A, %B %-d' }}_

[Guidelines]({% link _assignments/final-project.md %}#project-website)

### Poster

_Due date_: Must be printed and posted electronically to your GitHub and/or
website before the SoftDes final project Expo {{ site.data.dates.final_expo | date: '%A, %b %-d' }}

[Guidelines]({% link _assignments/final-project.md %}#demo-session-poster)

### Code

_Due date_: End of day {{ site.data.dates.final_expo | date: '%A, %b %-d' }}. Be sure to update your README file as
well.

[Guidelines]({% link _assignments/final-project.md %}#code-submission)

## Communicating with your audience

The work you've done in this class is potentially of interest to several
different groups of people. This exercise is intended to help you select what
content to include and prioritize in your website and other deliverables.

In groups at your tables:

1. Select three potential audiences you would like your work to reach. Examples include future employers, potential users, other developers continuing your work, SoftDes staff, students learning programming, media outlets, etc.
2. For each of the three groups you've chosen, discuss at your table what sort of information that audience wants to see. Make a list of their priorities.
3. Below are several of the final project websites from a previous year. Randomly choose at least three of them, visit each putting yourself in the shoes of each of your audience groups, and take notes on what you find. Were the details you were looking for easy to find? What was missing? Where did it excel and where could it be better?

<ul>
{% for project in site.data['final-projects'].sp2016 %}
{% assign mod = forloop.index | modulo: 2 %}
{% if mod == 1 %}
<li><a href="{{ project.website }}">{{ project.name }}</a></li>
{% endif %}
{% endfor %}
</ul>
