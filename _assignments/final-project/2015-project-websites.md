---
title: Past Project Websites
date: 2016-12-29 13:26:01 -05:00
description: ''
parent: final-project
---

The following list of final project websites is from Software Design in Spring
2015 (in no particular order).

_Note_: In 2015, the technical review deliverables were submitted via the
project website, so you will likely see that material on many of these sites.
We do not have this requirement in 2017, though you will likely use content
from those deliverables to help create your site.

{% for project in site.data['final-projects'].sp2015 %}
* [{{ project.name }}]({{ project.website }}){% endfor %}
