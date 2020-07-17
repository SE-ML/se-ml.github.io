---
layout: post
title:
comments: False
permalink: /members
---

<div>
  <img src="/assets/img/team.png" class="blog-image">
</div>

<br><br>
{% assign sorted_staff = site.staff | sort:"index" %}
More information:
<ul>
  {% for st in sorted_staff %}
    <li>
      <a href="{{st.webpage}}" target="_blank">{{ st.first_name }} {{ st.last_name }}</a>
    </li>
  {% endfor %}
</ul>