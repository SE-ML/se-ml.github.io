---
layout: default
permalink: /practices
---

<h1 class="black"> Engineering best practices for Machine Learning </h1>


 <div class="large-image">
      <img src="/assets/img/SE4ML-practices-diagram.png" class="blog-image">
</div>
<br>
The list below gathers a set of engineering best practices for
developing software systems with machine learning (ML) components.
<br><br>
These practices were identified by engaging with ML engineering teams and
reviewing relevant <a href="https://github.com/SE-ML/awesome-seml/blob/master/readme.md" target="blank"> academic and grey literature</a>.
We are constantly running a <a href="https://se-ml.github.io/survey/" target="blank"> global survey</a>
among ML engineering teams to measure the adoption of these practices.
<br><br>
The various practices are grouped into 6 categories, as illustrated in the diagram above.

{% assign sorted_practices = site.categories.best_practices  | sort:"index" %}


<h3 class="black bold" id="data"> Data </h3>


"Whoever owns the data pipeline will own the production pipeline for machine learning."
--<a href="https://twitter.com/chipro/status/1232105910631157761">Chip Huyen<a>

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Data' %}
        <li>
          <a  href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>



<h3 class="black bold" id="experiment"> Training </h3>

"No amount of experimentation can ever prove me right; a single experiment can prove me wrong." --Albert Einstein

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Experiment' %}
        <li>
          <a  href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>



<h3  class="black bold" id="coding"> Coding </h3>

"You can’t be an AI expert these days and not have some grounding in software engineering."
--<a href="https://twitter.com/Grady_Booch/status/1004078706518736896">Grady Booch</a>

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Coding' %}
        <li>
          <a   href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>



<h3 class="black bold" id="deployment"> Deployment </h3>

“If your model isn’t deployed into production, does it really exist?”
--<a href="https://twitter.com/code_star/status/1041913975154331648">Anonymous<a>

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Deployment' %}
        <li>
          <a  href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>


<h3 class="black bold" id="team"> Team </h3>

"If you want to go fast, go alone; but if you want to go far, go together." -- African proverb, allegedly

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Team' %}
        <li>
          <a  href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>


<h3 class="black bold" id="governance"> Governance </h3>

"Where there is great power there is great responsibility."
--<a href="https://quoteinvestigator.com/2015/07/23/great-power/">Winston Churchill<a>

<ul>
  {% for pr in sorted_practices %}
     {% if pr.category == 'Governance' %}
        <li>
          <a  href="{{pr.url}}">{{ pr.name }}</a>
        </li>
    {% endif %}

  {% endfor %}
</ul>