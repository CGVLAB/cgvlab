---
title: "CGVLab - Team"
layout: gridlay
excerpt: "CGVLab: Team members"
sitemap: false
permalink: /team/
---

# Group Members
{% assign img_width = '128px' %}
{% assign img_height = '128px' %}

Jump to [faculty](#faculty), [graduate students](#graduate-students), [former members](#former-members).

## Faculty
{% assign number_printed = 0 %}
{% for member in site.data.faculty %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if member.photo %}
{% assign photo_link = site.dir_resources_images | append: '/teampic/' | append: member.photo %}
{% else %}
{% assign photo_link = site.dir_theme_images | append: '/bio-photo.jpg' %}
{% endif %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ photo_link }}" class="img-responsive" style="object-fit: cover; width: {{ img_width }}; height: {{ img_height }}; float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }}</i><br>
  {% if member.url %}
  <i><a href="{{ member.url }}" target="_blank">Website</a></i>
  {% endif %}

</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Graduate Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if member.photo %}
{% assign photo_link = site.dir_resources_images | append: '/teampic/' | append: member.photo %}
{% else %}
{% assign photo_link = site.dir_theme_images | append: '/bio-photo.jpg' %}
{% endif %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ photo_link }}" class="img-responsive" style="object-fit: cover; width: {{ img_width }}; height: {{ img_height }}; float: left" />
  <h4>{{ member.name }}</h4>
  {% if member.url %}
  <i><a href="{{ member.url }}" target="_blank">Website</a></i>
  {% endif %}
  {% if member.linkedin %}
  <i><a href="{{ member.linkedin }}" target="_blank">LinkedIn</a></i>
  {% endif %}
  
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Former members

{% assign number_printed = 0 %}
{% for member in site.data.former_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if member.photo %}
{% assign photo_link = site.dir_resources_images | append: '/teampic/' | append: member.photo %}
{% else %}
{% assign photo_link = site.dir_theme_images | append: '/bio-photo.jpg' %}
{% endif %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ photo_link }}" class="img-responsive" style="object-fit: cover; width: {{ img_width }}; height: {{ img_height }}; float: left" />
  {% if member.url %}
  <h4><a href="{{ member.url }}" target="_blank">{{ member.name }}</a></h4>
  {% else %}
  <h4>{{ member.name }}</h4>
  {% endif %}
  <i>{{ member.info }}</i><br>
  {% if member.linkedin %}
  <a href="{{ member.linkedin }}" target="_blank">LinkedIn</a>
  {% endif %}
  
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
