---
layout: practice
author: Alex Serban, Joost Visser
name: Use Sanity Checks for All External Data Sources
category: Data
unique_id: data_sanity
index: 1
difficulty: #
comments: True
references: ["DMP","MLOps","DQML"]
description:
image: #
photocredit: #

intent: Avoid invalid or incomplete data being processed. #
motivation: Data is at the heart of any machine learning model. Therefore, having the right data is crucial for model quality. #
applicability: #
related: #
dependencies: #
survey_question: Q32
---

Whenever using external data sources, or collecting data that may be incomplete or ill formated, it is important to perform sanity checks.
<!-- before using it. -->
Invalid or incomplete data may cause outages in production or lead to innacurate models.

Start by checking simple data attributes, such as:

- data types,
- missing values,
- data min. or max. values,
- histograms of continuous values,

and gradually include more complex data statistics, such as the ones recommended <a href="/blog/2020/input_data_completeness">here</a>.
