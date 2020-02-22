---
layout: practice
author: Alex Serban
name: Write Reusable Scripts for Data Cleaning and Merging
category: data_management
index: 3
difficulty: #
references: ["DMP", "MLOps", "BPMLI"]
comments: True
description:
image: #
photocredit: #
---

Most of the times, training machine learning models is preceeded by an exploratory phase, in which non-structured code is written in order to get the data in the right format or merge several data sources.
Especially when using notebooks, there is a tendency to write ad-hoc data processing scripts, which depend on variables that stored in memory during the execution.

Before moving to the experimentation phase, it is important to convert this code into reusable code -- e.g. by transforming the pieces of code into methods.