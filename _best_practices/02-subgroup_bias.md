---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Assess and Manage Subgroup Bias
category: Training
index: 22
unique_id: subgroup_bias
difficulty: "advanced"
references: [PFG, MCCIM]
comments: True
description:
image: #
photocredit: #

intent: Avoid bias and unfair decisions within subgroups. #
motivation: Ensuring fairness between two groups can lead to violations within subgroups. #
applicability: Subgroup bias should be assessed and managed for all applications which process data regarding groups and subgroups of individuals. #
related: [social_bias,discriminatory_attributes,risk] #
dependencies: #
survey_question: Q95 #
survey_item: We run tests to assess and manage subgroup bias (regarding e.g. gender or ethnicity).

labels: [fairness]

---

Subgroup bias can arise from improperly divided groups, often defined in order to avoid group bias, or due to a lack of data.
For example, consider an application where we divide the data based on location in New York and Amsterdam.
After division, it may be the case that we only have data where the population of New York is predominantly female, and the population of Amsterdam is predominantly male.
This division introduces a subgroup bias, which ultimately leads to socially biased models.

In order to avoid subgroup bias, it is imperative to test, assess and calibrate the models as in the case of <a href="/best_practices/01-social_bias/">social bias</a>.

Follow the references in order to learn more about technical approaches to ensure fair predictions for every sub-population which can be identified in a set of groups.
