---
title: Instructors
weight: 30
---

{% for instructor in site.data.course.instructors %}
{{ instructor.name}} <{{ instructor.email }}> ({{ instructor.office }}{% if instructor.website %}, [{{ instructor.website }}]({{ instructor.website }}){% endif %}). Office hours by request.
{% endfor %}

NINJAs: {{ site.data.course.assistants | map: 'name' | join: ', ' }}

Ninja office hour times are posted on
[Piazza](https://piazza.com/class/iy3bgqkraq97c0?cid=17). If you need help
outside of hours and class, please use [Slack](https://{{ site.slack.team }}.slack.com/messages/{{ site.slack.channel }})!
