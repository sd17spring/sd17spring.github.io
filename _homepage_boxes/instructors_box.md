---
title: Teaching Tea
position: 5
---

{% for instructor in site.data.course.instructors %}
**{{ instructor.name}}** [&lt;{{ instructor.email }}&gt;](mailto:{{ instructor.email }}), {{ instructor.office }}{% if instructor.website %}, [website]({{ instructor.website }}){% endif %}.
{% endfor %}

**NINJAs**: {{ site.data.course.assistants | map: 'name' | join: ', ' }}

Ninja office hour times are posted on
[Piazza](https://piazza.com/class/iy3bgqkraq97c0?cid=17).

<iframe src="https://docs.google.com/spreadsheets/d/1n1hu2Pi_HmkT91HpOgOqtyDYezA4QhHlhPDfoVhOPz4/pubhtml?gid=0&single=true&headers=false&widget=true"></iframe>
