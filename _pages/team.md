---
title: "CGVLab - Team"
layout: gridlay
excerpt: "CGVLab: Team members"
sitemap: false
permalink: /team/
---

# Group Members
Jump to [faculty](#faculty), [graduate students](#graduate-students), [former members](#former-members).

## Faculty

<div class="container-fluid">
  <div class="row">
    {% for member in site.data.faculty %}
    {% include member.html member = member %}
    {% endfor %}
  </div>
</div>

## Graduate Students

<div class="container-fluid">
  <div class="row">
    {% for member in site.data.students %}
    {% include member.html member = member %}
    {% endfor %}
  </div>
</div>

## Former Members

<div class="container-fluid">
  <div class="row">
    {% for member in site.data.former_members %}
    {% include member.html member = member %}
    {% endfor %}
  </div>
</div>
