---
title: "Publications"
layout: content
permalink: /publications/
---

<!-- Code for publication searching !-->
<script>
    // Publication search values

    // Array of publications
    var publications = [];
    // State of publication IDs (loaded or not loaded)
    var publicationsLoaded = false;
</script>

# Publications

## Search

{% include search.html %}

<hr>

## Highlights

(For a full list see [below](#full-list).)

<div id="highlighted" class="container-fluid">
{% bibliography --query @*[highlighted=true] --template reference %}
</div>
<div id="highlighted-empty" class="container-fluid p-0" style="display: none">
<h3 class="text-muted">No publications</h3>
</div>

<hr>

## Full List

{% for publication_year in (2000..2020) reversed %}
{% if forloop.last %}

<h3 id="previous">Pre-{{ publication_year | plus: 1 }}</h3>
<div class="container-fluid">
{% bibliography --query @*[year<={{publication_year}},highlighted!=true] --template reference %}
</div>
{% else %}
<h3 id="year-{{ publication_year }}">{{ publication_year }}</h3>
<div class="container-fluid">
{% bibliography --query @*[year={{publication_year}},highlighted!=true] --template reference %}
</div>
{% endif %}
{% endfor %}
<div id="full-empty" class="container-fluid p-0" style="display: none">
<h3 class="text-muted">No publications</h3>
</div>

<!-- Code for publication searching !-->
<!-- Relies on variables declared in `search.html` !-->
<script>
  // Removes DOI from reference (if enabled)

  const removeDoi = false;

  if (removeDoi) {
    for (var i = 0; i < publications.length; i++) {
      var reference = $('#' + (publications[i] || '')).children();
      for (var j = 0; j < reference.length; j++)
        reference[j].innerHTML = reference[j].innerHTML.replace(/(https?:\/\/)?doi.org\S+/gim, '');
    }
  }

  // Set publication status as loaded
  publicationsLoaded = true;

  // Enable search bar
  $('#searchBar').show();
</script>
