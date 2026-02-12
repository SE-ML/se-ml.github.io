---
layout: default
permalink: /publications
---

<h3 class="black"> Our publications: </h3>


<ul>
  {% assign sorted_pub = site.pub | sort: 'date' | reverse  %}
  {% for item in sorted_pub %}
    <li>
      <a href="{{item.webpage}}">{{item.title}}</a>
    </li>
  {% endfor %}
</ul>