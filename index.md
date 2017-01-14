---
date: '2016-12-29T18:26:01'
description: ''
title: Software Design Spring 2016
layout: splash
permalink: /
---

{% include toc %}

## Instructors

{% for instructor in site.data.course.instructors %}
{{ instructor.name}} ({{ instructor.email}}, {{ instructor.office}}{% if instructor.website %}, [{{ instructor.website }}]({{ instructor.website }}){% endif %})
{% endfor %}


## NINJAs

{{ site.data.course.assistants | map: 'name' | join: ', ' }}


## Meeting Times

{% for section in site.data.course.sections %}
Section {{ section.number }}: {{ section.when }} in {{ section.where }}
{% endfor %}


## Textbook

_Think Python_ by Allen Downey (available free
[online](http://www.greenteapress.com/thinkpython/) or in hardcopy from
various online retailers)


{% if site.course.piazza_url %}
## Piazza

All communication for this class will be through
[Piazza]({{site.course.piazza_url}}). There is no mailing
list.
{% endif %}


## GitHub

Assignments will be distributed and submitted via
[GitHub](https://github.com/{{site.course.github_owner}}).


{% if site.course.flootbits_url %}
## Floobits

We often share in-class code interactively using
[Floobits]({{site.course.flootbits_url}}). You can sign up with your GitHub
account.
{% endif %}


## Office Hours

Office hour times will be posted on
[Piazza](({{site.course.piazza_url}})/staff). If you need help
outside of hours and class, please fill [this](http://tinyurl.com/softdeshelp)
out!



## Useful Resources

Several [useful resources](/resources) for the class are collected
[here](/resources). A few
[tutorials](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)
were also created by the NINJAs for the Spring 2014 class.[
](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)





