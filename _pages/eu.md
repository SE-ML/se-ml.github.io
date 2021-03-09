---
layout: post
title: EU Guidelines for Trustworthy AI
comments: False
permalink: /eu
image: /assets/img/eu.jpg
photocredit: Requirements for trustworthy AI from the High-Level expert group on AI setup by the EU Commission.
---


In order to avoid unintentional harm that improper development of AI technologies can have on the society, the European Commission, through the High-Level expert group on AI, published a series guidelines and checklists for development of trustworthy AI.

By analysing the guidelines, we found out they do not specify actions to be taken by those involved in building AI systems.
In order to increase the actionability of the guidelines, we made efforts to extend our catalogue of practices with new practices that address the EU requirements for trustworthy AI.

In particular, we focused on a major sub-field of AI, called machine learning (ML).
By analysing the academic and grey literature, we extracted 14 operational practices for trustworthy ML that address the 7 requirements for trustworthy AI from the picture above as follows:

{% assign sorted_practices = site.best_practices  | sort:"index" %}

#### Human agency and oversight
<img class="hover-me" src="https://img.shields.io/badge/EU-Human%20Agency-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  <!-- {{pr.labels}} -->
  {% if pr.labels contains 'agency' %}
     <li> <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

#### Technical robustness and safety
<img class="hover-me" src="https://img.shields.io/badge/EU-Robustness-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  {% if pr.labels contains 'robustness' %}
    <li>  <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

#### Privacy and Data Governance
<img class="hover-me" src="https://img.shields.io/badge/EU-Privacy-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  {% if pr.labels contains 'privacy' %}
    <li>  <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

#### Transparency
<img class="hover-me" src="https://img.shields.io/badge/EU-Transparency-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  {% if pr.labels contains 'transparency' %}
    <li>  <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>


#### Diversity, Non-Discrimination and Fairness
<img class="hover-me" src="https://img.shields.io/badge/EU-Fairness-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  {% if pr.labels contains 'fairness' %}
    <li>  <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

#### Accountability
<img class="hover-me" src="https://img.shields.io/badge/EU-Accountability-lightgrey?labelColor=003399">
<ul>
{% for pr in sorted_practices %}
  {% if pr.labels contains 'accountability' %}
    <li>  <a href="{{pr.url}}">{{ pr.name }}</a> </li>
  {% endif %}
{% endfor %}
</ul>

