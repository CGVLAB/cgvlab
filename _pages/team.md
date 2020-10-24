---
title: "CGVLab - Team"
layout: gridlay
excerpt: "CGVLab: Team members"
sitemap: false
permalink: /team/
---

{% assign members_per_row = 3 %}

# Group Members
Jump to [faculty](#faculty), [graduate students](#graduate-students), [former members](#former-members).

## Faculty

<div class="container-fluid">
  <div class="row">
{% assign member_count = 0 %}
{% for member in site.data.faculty %}
{% assign member_should_new_row = member_count | modulo: members_per_row %}
{% if member_should_new_row == 0 %}
{% endif %}
{% include member.html member = member %}
{% assign member_should_close_row = member_count | plus: 1 | modulo: members_per_row %}
{% if member_should_close_row == 0 %}
{% endif %}
{% assign member_count = member_count | plus: 1 %}
{% endfor %}
</div>
</div>

## Graduate Students

<div class="container-fluid">
{% for member in site.data.students %}
{% include member.html member = member %}
{% endfor %}
</div>

## Former Members

<div class="container-fluid">
{% for member in site.data.former_members %}
{% include member.html member = member %}
{% endfor %}
</div>
