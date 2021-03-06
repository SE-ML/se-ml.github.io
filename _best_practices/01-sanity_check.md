---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Sanity Checks for All External Data Sources
title: Use Sanity Checks for All External Data Sources
category: Data
unique_id: data_sanity
index: 1
difficulty: "medium"
comments: True
references: ["DMP","MLOps"]
description:
image: #
photocredit: #

intent: Avoid invalid or incomplete data being processed. #
motivation: Data is at the heart of any machine learning model. Therefore, avoiding data errors is crucial for model quality. #
applicability: Data quality control should be applied to any machine learning application. #
related: [data_complete, data_reusable] #
dependencies: #
survey_question: Q32

labels:

---

Whenever external data sources are used, or data is collected that may be incomplete or ill formatted, it is important to verify the data quality.
Invalid or incomplete data may cause outages in production or lead to inaccurate models.

Start by checking simple data attributes, such as:

- data types,
- missing values,
- data min. or max. values,
- histograms of continuous values,

and gradually include more complex data statistics, such as the ones recommended <a href="/best_practices/01-input-data-complete/">here</a>.


Missing data can also be substituted using data <a href="https://en.wikipedia.org/wiki/Imputation_%28statistics%29">imputation</a>; such as imputation by zero, mean, median, random values, etc.

Also, make sure the data verification scripts are <a href="/best_practices/01-reusable_data_clean/">reusable</a> and can be later integrated in any processing pipeline.
