---
title: Instructors
position: 5
---

{% for instructor in site.data.course.instructors %}
**{{ instructor.name}}** [&lt;{{ instructor.email }}&gt;](mailto:{{ instructor.email }}), {{ instructor.office }}{% if instructor.website %}, [website]({{ instructor.website }}){% endif %}.
{% endfor %}

**NINJAs**: {{ site.data.course.assistants | map: 'name' | join: ', ' }}
