---
date: 2017-02-12
layout: splash
permalink: /
title: Software Design Spring 2017
header:
  overlay_color: "#444"
  overlay_filter: "0.5"
  # overlay_image: /assets/images/unsplash-image-1.jpg
  # cta_label: "Download"
  # cta_url: "https://github.com/mmistakes/minimal-mistakes/"
  # caption: "Photo credit: [**Unsplash**](https://unsplash.com)"
# excerpt: "Bacon ipsum dolor sit amet salami ham hock ham, hamburger corned beef short ribs kielbasa biltong t-bone drumstick tri-tip tail sirloin pork chop."
---


<div class="feature__wrapper">

<div class="feature__item"><div class="archive__item"><div class="archive__item-body">
<h2 class="archive__item-title">Due Soon</h2>
<div class="archive__item-excerpt" markdown="1">
Reading journal, Think Python 11, 12 is due Monday 2/13.

[Mini Project 2: Computational Art]({% link _assignments/mini-project-2-computational-art.md %}) is due Monday 2/13. Place your work in `{{ mp2_gallery_public_drive_path }}` on the Olin Public by 1pm today to enter it in the [In-Class Gallery Show]({% link _assignments/mini-project-2-computational-art.md %}#optional-in-class-gallery-show).

[Project toolbox]({% link _pages/toolboxes.md %}) exercises have been launched.
You will do at least five in total, at least three of which must be completed before spring break.

See the [Assignments]({% link _pages/assignments.html %}) page and the [course calendar]({% link _pages/calendar.md %}) for a list of all due dates.
</div></div></div></div>

<div class="feature__item"><div class="archive__item"><div class="archive__item-body">
<h2 class="archive__item-title">Communication</h2>
<div class="archive__item-excerpt" markdown="1">
Communication for this class is through [Piazza]({{ site.course.piazza_url }});
and the [#softdes17spring channel](https://{{ site.slack.team }}.slack.com/messages/{{ site.slack.channel }}) of the
[Olin Slack team](https://{{ site.slack.team }}.slack.com/).

Assignments will be distributed and submitted via
[GitHub](https://github.com/{{site.course.github_owner}}).

</div></div></div></div>

<div class="feature__item"><div class="archive__item"><div class="archive__item-body">
<h2 class="archive__item-title">Instructors</h2>
<div class="archive__item-excerpt" markdown="1">
{% for instructor in site.data.course.instructors %}
{{ instructor.name}} <{{ instructor.email }}> ({{ instructor.office }}{% if instructor.website %}, [{{ instructor.website }}]({{ instructor.website }}){% endif %})
{% endfor %}

Ninjas: {{ site.data.course.assistants | map: 'name' | join: ', ' }}

Ninja office hour times are posted on
[Piazza](https://piazza.com/class/iy3bgqkraq97c0?cid=17). If you need help
outside of hours and class, please use [Slack](https://olin.slack.com/messages/softdes17spring/)!
</div></div></div></div>

</div>

<div class="feature__wrapper">

<div class="feature__item"><div class="archive__item"><div class="archive__item-body">
<h2 class="archive__item-title">Resources</h2>
<div class="archive__item-excerpt" markdown="1">
Several [useful resources]({% link _pages/resources.md %}) for the class are collected
[here]({% link _pages/resources.md %}). A few
[tutorials](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)
were also created by the NINJAs for the Spring 2014 class.[
](https://drive.google.com/folderview?id=0B6xCjnZeUlbMY3M5Y3N3aU9scGM&usp=sharing)
</div></div></div></div>

<div class="feature__item"><div class="archive__item"><div class="archive__item-body">
<h2 class="archive__item-title">Textbook</h2>
<div class="archive__item-excerpt" markdown="1">
_Think Python_ by Allen Downey (available free
[online](http://greenteapress.com/wp/think-python-2e/) or in hardcopy from
various online retailers)
</div></div></div></div>

</div>
