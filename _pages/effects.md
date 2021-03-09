---
layout: post
title: Effects of the practices
comments: False
permalink: /effects
---


Using the [survey](/survey) responses, we analysed the relationship between sets of practices and four desired effects.
We found out that the effect can be predicted with high accuracy from the following sets of practices (read more about the method in our [publication](https://arxiv.org/abs/2007.14130)).



{% assign sorted_practices = site.best_practices  | sort:"index" %}

#### Agility
<img class="hover-me" src="https://img.shields.io/badge/Effect-Agility-lightgrey?labelColor=1F4DAF">
<ul>
{% for pr in sorted_practices %}
  <!-- {{pr.labels}} -->
  {% if pr.labels contains 'agility' %}
     <li> <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

#### Software quality
<img class="hover-me" src="https://img.shields.io/badge/Effect-Quality-lightgrey?labelColor=1F4DAF">
<ul>
{% for pr in sorted_practices %}
  <!-- {{pr.labels}} -->
  {% if pr.labels contains 'quality' %}
     <li> <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>


#### Team Effectiveness
<img class="hover-me" src="https://img.shields.io/badge/Effect-Effectiveness-lightgrey?labelColor=1F4DAF">
<ul>
{% for pr in sorted_practices %}
  <!-- {{pr.labels}} -->
  {% if pr.labels contains 'effectiveness' %}
     <li> <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>


#### Traceability
<img class="hover-me" src="https://img.shields.io/badge/Effect-Traceability-lightgrey?labelColor=1F4DAF">
<ul>
{% for pr in sorted_practices %}
  <!-- {{pr.labels}} -->
  {% if pr.labels contains 'traceability' %}
     <li> <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>