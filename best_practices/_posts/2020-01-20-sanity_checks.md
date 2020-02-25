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
motivation: Data is at the heart of any machine learning model. Therefore, avoiding data errors is crucial for model quality. #
applicability: #
related: [data_complete, data_reusable] #
dependencies: #
survey_question: Q32
---

Whenever using external data sources, or collecting data that may be incomplete or ill formatted, it is important to verify its quality.
Invalid or incomplete data may cause outages in production or lead to inaccurate models.

Start by checking simple data attributes, such as:

- data types,
- missing values,
- data min. or max. values,
- histograms of continuous values,

and gradually include more complex data statistics, such as the ones recommended <a href="/blog/2020/input_data_completeness">here</a>.


Also, make sure the data verification scripts are <a href="/blog/2020/reusable_data_cleaning/" target="blank">reusable</a> and can be later integrated in a processing pipeline.
