---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Perform Checks to Detect Skew between Models
title: Perform Checks to Detect Skew between Models
category: Deployment
unique_id: deployment_distskew
index: 31
difficulty: "advanced"
references: [Rs4ML, CD4ML, TDBML, TFX]
comments: True
description:
image: #
photocredit: #

intent: Avoid introducing errors in production pipelines. #
motivation: Test if a model that performs well during training and initial testing will also perform well in production i.e. test if the training data distribution reflects the production one. #
applicability: Model skew should be monitored in any production-level machine learning application.
related:  [deployment_automate, deployment_monitor] #
dependencies: #
survey_question: Q61

labels:

---

In a quickly changing environment or when the training data does not reflect the production distribution, it is not uncommon to have models that perform well during training and initial testing, but not in production.
In order to avoid deployment of under-performing or sub-optimal models, it is recommended to continuously check possible skew between the production and training environments.

Make sure to:
- check performance skew between training and hold-out data,
- check skew between data generated in previous days,
- check skew between live data and training.