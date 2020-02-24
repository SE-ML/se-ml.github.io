---
layout: practice
author: Alex Serban, Joost Visser
name: Write Reusable Scripts for Data Cleaning and Merging
category: Data
id: data_reusable
index: 3
difficulty: #
references: ["DMP", "MLOps", "BPMLI"]
comments: True
description:
image: #
photocredit: #

intent: Avoid messy data mugging scripts, reuse code and increase reproducibility. #
motivation: Data cleaning and merging are exploratory processes and tend to be less structured. Many times these processes involve manual steps or poorly structured code which can not be later reused.  #
applicability: #
related: #
dependencies: #
survey_question: Q34
---

Most of the times, training machine learning models is preceeded by an exploratory phase, in which non-structured code is written or manual steps are performed in order to get the data in the right format or merge several data sources.
Especially when using notebooks, there is a tendency to write ad-hoc data processing scripts, which depend on variables already stored in memory running previous cells.

Before moving to the training phase, it is important to convert this code into reusable scripts and move it into methods which can be called invididually and *tested*.