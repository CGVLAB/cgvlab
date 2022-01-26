---
title: "Research"
layout: content
permalink: /research/
---

# Research

{% for research in site.data.research %}
<h2>{{ research.title }}</h2>
<p>{{ research.description }}</p>
{% if research.image %}
<img src="{{ site.dir_resources_images }}/{{ research.image }}" alt="Image for project {{ research.title }}" />
{% endif %}
{% endfor %}
