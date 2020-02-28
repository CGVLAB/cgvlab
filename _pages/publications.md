---
title: "CGVLab - Publications"
layout: gridlay
excerpt: "CGVLab -- Publications."
sitemap: false
permalink: /publications/
---

# Testing bibtex

{% bibliography --file my_test_bib_file %}



# Publications

## Highlights

(For a full list see [below](#full-list).

{% assign year_sorted_pubs = (site.data.publist | sort: 'year') | reverse %}

{% assign number_printed = 0 %}
{% for publi in year_sorted_pubs %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }} ({{ publi.year }}) </pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## Full List

<div class="row">

<div class="col-sm-6 clearfix">
<h4>By year:</h4>
{% for publi in year_sorted_pubs %}
  {{ publi.title }} ({{ publi.year }}) <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>
{% endfor %}
</div>

<div class="col-sm-6 clearfix">
<h4>By title:</h4>
{% assign title_sorted_pubs = (site.data.publist | sort: 'title') %}
{% for publi in title_sorted_pubs %}
  {{ publi.title }} ({{ publi.year }}) <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>
{% endfor %}
</div>

</div>