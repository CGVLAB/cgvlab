---
title: "Team"
layout: content
permalink: /team/
---

# Team

Jump to [faculty](#faculty), [graduate students](#graduate-students),
[former members](#former-members).

## Faculty

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% for person in site.data.faculty %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>

## Graduate Students

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% for person in site.data.students %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>

## Former Students

<div class="container-fluid lab-no-space">
  <div class="card-columns">
    {% for person in site.data.former_members %}
    {% include member.html person = person %}
    {% endfor %}
  </div>
</div>
