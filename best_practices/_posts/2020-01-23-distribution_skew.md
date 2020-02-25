---
layout: practice
author: Alex Serban, Joost Visser
name: Perform Checks to Detect Skews between Models
category: Deployment
unique_id: deployment_distskew
index: 23
difficulty: #
references: [Rs4ML, CD4ML, TDBML, TFX]
comments: True
description:
image: #
photocredit: #

intent: Avoid introducing errors in production pipelines. #
motivation: Test if a model that performs well during training and initial testing will also perform well in production i.e. test if the training data distribution reflects the production one. #
applicability: #
related:  [deployment_automate, deployment_monitor] #
dependencies: #
survey_question: Q61
---

In a fast changing environment or if the training data does not reflect the production distribution, it is not uncommon to have models that perform well during training and initial testing, but not in production.
In order to avoid deployment of under-performing or sub-optimal models, it is recommended to check possible skews between  the production and training environments.

Make sure to:
- check performance skews between training and hold-out data,
- check skews between data generated in previous days,
- check skews between live data and training.