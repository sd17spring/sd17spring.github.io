---
title: Instructors
position: 5
---

{% for instructor in site.data.course.instructors %}
{{ instructor.name}} <{{ instructor.email }}> ({{ instructor.office }}{% if instructor.website %}, [{{ instructor.website }}]({{ instructor.website }}){% endif %}). Office hours by request.
{% endfor %}

NINJAs: {{ site.data.course.assistants | map: 'name' | join: ', ' }}
