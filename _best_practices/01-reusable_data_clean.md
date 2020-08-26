---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Write Reusable Scripts for Data Cleaning and Merging
category: Data
unique_id: data_reusable
index: 4
difficulty: "basic"
references: ["DMP", "MLOps", "BPMLI"]
comments: True
description:
image: #
photocredit: #

intent: Avoid untidy data wrangling scripts, reuse code and increase reproducibility. #
motivation: Data cleaning and merging are exploratory processes and tend to be less structured. Many times these processes involve manual steps or poorly structured code which can not be reused later or integrated in a pipeline.  #
applicability: Reusable data cleaning scripts should be written for any ML application that does not use raw or standard data sets.
related: [exp_tstfeature, coding_regr] #
dependencies: #
survey_question: Q34
---

Most of the time, training machine learning models is preceded by an exploratory phase, in which non-structured code is written or manual steps are performed in order to get the data in the right format, or merge several data sources.
Especially when using notebooks, there is a tendency to write ad-hoc data processing scripts, which depend on variables already stored in memory when running previous cells.

Before moving to the training phase, it is important to convert this code into reusable scripts and move it into methods which can be called and *tested* individually.
This will enable code reuse and ease integration into processing pipelines.