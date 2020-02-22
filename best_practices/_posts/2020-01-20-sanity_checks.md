---
layout: practice
author: Alex Serban
name: Sanity Check All External Data Sources
category: data_management
index: 1
difficulty: #
comments: True
references: ["DMP","MLOps","DQML"]
description:
image: #
photocredit: #
---

Data is at the heart of any machine learning model.
Therefore, having the right data is crucial for model quality.

Whenever using external data sources, or collect data that may be incomplete or ill formated, it is important to sanity check it before using it.
Invalid or incomplete data may cause outages in production or lead to <> models.

Start by checking simple data attributes, such as:

- missing values
- data min. or max. values
- histograms of continuous values

And gradually include more complex data statistics, such as:
- check if a feature is present in enough examples
- check if a feature has the right number of values (cardinality) e.g. there can not be more than an age / age derived feature
- check hidden dependencies between data attributes

Lastly, building a strong sanity check pipeline should include *visuals* or *dashboards* to continuously monitor data quality and raise *alerts* for unusual events.

If your model performs close to real-time or online learning, a strong alert system can help to detect errors early and correct them.
