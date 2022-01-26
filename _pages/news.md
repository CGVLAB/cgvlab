---
title: "News"
layout: content
permalink: /news/
---

# News

{% for article in site.data.news %}
<p>{{ article.date }} <br />
<em>{{ article.headline }}</em></p>
{% endfor %}
