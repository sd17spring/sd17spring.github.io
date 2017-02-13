---
date: 2017-01-21 20:46:57 -0500
description: ''
permalink: /
title: Software Design Spring 2017
---

{% include toc %}

## News

Tomorrow is [day 8]({% link _days/day-8.md %}).

### Coming Up

* Reading journal, Think Python 11, 12 due Monday 2/9 (but starting earlier is great)
* [Project toolbox]({% link _pages/toolboxes.md %}) exercises have been launched.
You will do at least five in total, at least three of which must be completed before spring break.

## Instructors

{% for instructor in site.data.course.instructors %}
{{ instructor.name}} ({{ instructor.email}}, {{ instructor.office}}{% if instructor.website %}, [{{ instructor.website }}]({{ instructor.website }}){% endif %})
{% endfor %}


## NINJAs

{{ site.data.course.assistants | map: 'name' | join: ', ' }}


## Meeting Times

Both sections:

* Meet Mon/Thu 1:30-3:10pm in AC326
* Break-out to AC328 for more studio space


## Textbook

_Think Python_ by Allen Downey (available free
[online](http://greenteapress.com/wp/think-python-2e/) or in hardcopy from
various online retailers)


{% if site.course.piazza_url %}
## Communication

All communication for this class will be through [Piazza]({{ site.course.piazza_url }})
and the [#softdes17spring channel](https://{{ site.slack.team }}.slack.com/messages/{{ site.slack.channel }}) of the
[Olin Slack team](https://{{ site.slack.team }}.slack.com/).
There is no mailing list.
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

Office hour times are posted on
[Piazza](https://piazza.com/class/iy3bgqkraq97c0?cid=17). If you need help
outside of hours and class, please use [Slack](https://olin.slack.com/messages/softdes17spring/)!



## Useful Resources

Several [useful resources]({% link _pages/resources.md %}) for the class are collected
[here]({% link _pages/resources.md %}). A few
[tutorials](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)
were also created by the NINJAs for the Spring 2014 class.[
](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)
