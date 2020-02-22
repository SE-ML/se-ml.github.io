---
layout: practice
author: Alex Serban
name: Use Sanity Checks for All External Data Sources
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

Whenever using external data sources, or collect data that may be incomplete or ill formated, it is important to perform sanity checks before using it.
Invalid or incomplete data may cause outages in production or lead to innacurate models.

Start by checking simple data attributes, such as:

- data types,
- missing values,
- data min. or max. values,
- histograms of continuous values,

and gradually include more complex data statistics, such as the ones recommended <a href="/blog/2020/input_data_completeness">here</a>.
