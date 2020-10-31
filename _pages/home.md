---
title: "CGVLab - Home"
layout: home
excerpt: "CGVLab at Purdue University."
sitemap: false
permalink: /
---

# Welcome to the CGVLab

<div class="container m-0 p-0 justify-content-start">
<div id="homeCarousel" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    {% assign indicator_count = 0 %}
    {% for item in site.data.carousel %}
    {% if indicator_count == 0 %}
    <li data-target="#homeCarousel" data-slide-to="{{ indicator_count }}" 
     class="{{ indicator_class }}"></li>
    {% else %}
    <li data-target="#homeCarousel" data-slide-to="{{ indicator_count }}"></li>
    {% endif %}
    {% assign indicator_count = indicator_count | plus: 1 %}
    {% endfor %}
  </ol>
  <div class="carousel-inner">
    {% assign item_count = 0 %}
    {% for item in site.data.carousel %}
    {% if item_count == 0 %}
    <div class="carousel-item active">
    {% else %}
    <div class="carousel-item">
    {% endif %}
    <div class="p-2 bg-dark border border-dark rounded">
        <div class="embed-responsive embed-responsive-16by9">
            <img src="{{ site.dir_resources_images }}/{{ item.photo }}" class="embed-responsive-item card-img-top rounded" 
            style="object-fit: cover;" alt="{{ item.title }}">
        </div>
    </div>

    {% if item.title and item.caption %}
      <div class="carousel-caption d-none d-md-block rounded" style="background-color: rgba(0, 0, 0, 0.5)">
        <h5 style="font-weight-bold">{{ item.title }}</h5>
        <p>{{ item.caption }}</p>
      </div>
    {% endif %}
    </div>
    {% assign item_count = item_count | plus: 1 %}
    {% endfor %}
  </div>
  <a class="carousel-control-prev" href="#homeCarousel" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon cgv-slider-control"  aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#homeCarousel" role="button" data-slide="next">
    <span class="carousel-control-next-icon cgv-slider-control" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
</div>
<br>