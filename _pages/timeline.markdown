---
permalink: timeline.json
layout: 
---

{
  "title": {
    "text": {"headline": "SoftDes Assignments"}
  },
  "events": [
  {% for reading in site.data.readings %}
    {
      "start_date": {
        "day": {{ reading.due_date | date: "%-d" }},
        "month": {{ reading.due_date | date: '%-m' }},
        "year": {{ reading.due_date | date: '%Y' }}
      },
      "text": {
        "headline": {{ reading.summary | jsonify }},
        "text": {{ reading.description | jsonify }}
      },
      "group": "Readings"
    },
  {% endfor %}

  {% for event in site.assignments %}
  {% if event.due_date %}
    {% assign url = event.url | absolute_url %}
    {
      "start_date": {
        "day": {{ event.start_date | default: event.due_date | date: "%-d" }},
        "month": {{ event.start_date | default: event.due_date | date: '%-m' }},
        "year": {{ event.start_date | default: event.due_date | date: '%Y' }}
      },
      {% if event.start_date %}
      "end_date": {
        "day": {{ event.due_date | date: "%-d" }},
        "month": {{ event.due_date | date: '%-m' }},
        "year": {{ event.due_date | date: '%Y' }}
      },
      {% endif %}
      "text": {
        "headline": {{ event.title | strip | jsonify }},
        "text": {{ event.description | strip | append: ' ' | append: url | jsonify }}
      },
      "group": "Projects"
    },
  {% endif %}
  {% for part in event.parts %}
    {% assign url = event.url | absolute_url | append: '#' | append: part.tag %}
    {
      "start_date": {
        "day": {{ part.due_date | date: "%-d" }},
        "month": {{ part.due_date | date: '%-m' }},
        "year": {{ part.due_date | date: '%Y' }}
      },
      "text": {
        "headline": {{ part.name | jsonify }},
        "text": {{ part.name | prepend: ": " | prepend: event.title | append: ' ' | append: url | jsonify }}
      },
      "group": "Projects"
    },
  {% endfor %}
  {% endfor %}
  { "start_date": {"month":3, "day":13, "year":2017},
    "text": {"text": "Three Toolboxes"}, "group":"Toolboxes" },
  { "start_date": {"month":3, "day":28, "year":2017},
    "text": {"text": "Five Toolboxes"}, "group":"Toolboxes" },
  { "start_date": {
    "month": {{ site.course.dates.final_expo | date: "%-m" }},
    "day": {{ site.course.dates.final_expo | date: "%-d" }},
    "year": {{ site.course.dates.final_expo | date: "%Y" }}
    }, "text": {"text": "Expo"}, "group":"Projects" }
  ]
}
