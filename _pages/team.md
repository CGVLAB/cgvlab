---
title: "Team"
layout: content
permalink: /team/
---

# Team

Jump to [faculty](#faculty), [graduate students](#graduate-students),
[former members](#former-members).

<br>

## Faculty

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% assign faculty = site.data.faculty | lab_sort_last_name %}
    {% for person in faculty %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>

<br>

## Graduate Students

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% assign students = site.data.students | lab_sort_last_name %}
    {% for person in students %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>

<br>

## Former Members

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% assign former_members = site.data.former_members | lab_sort_last_name %}
    {% for person in former_members %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>
