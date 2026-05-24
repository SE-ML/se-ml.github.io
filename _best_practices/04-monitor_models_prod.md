---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Continuously Monitor the Behaviour of Deployed Models
title: Continuously Monitor the Behaviour of Deployed Models
category: Deployment
unique_id: deployment_monitor
index: 33
difficulty: "medium"
references: [CD4ML, MLPROD, MLLG, TFX, TDBML, MLOPMAP]
comments: True
description:
image: #
photocredit: #

intent: Avoid unintended behaviour in production models. #
motivation: Once a model is promoted to production, the team has to understand how it performs. #
applicability: Monitoring should be implemented in any production-level ML application.
related: [deployment_distskew, deployment_rollback, exp_quality, deployment_observability, deployment_data_pipeline_feedback] #
dependencies: #
survey_question: Q60

labels: [agility, traceability]

---

Monitoring plays an important role in production level machine learning.
Because the performance between training and production data can vary drastically, it is important to continuously monitor the behaviour of deployed models and raise alerts when unintended behaviour is observed.

The monitoring pipeline should include:
- performance, quality and skew metrics,
- fairness metrics,
- model interpretability outputs (e.g. <a href="https://arxiv.org/pdf/1602.04938v1.pdf">LIME</a>),
- metrics for the perceived effect of the model, e.g. user interactions, conversion rates, etc.

**Monitor the input data pipeline**
Model behaviour reflects the quality of the data it receives. Monitor the data pipeline itself, not just the model output:
- track feature distributions at ingestion time and alert on drift relative to the training baseline,
- detect missing, delayed, or malformed data feeds before they silently degrade model performance,
- measure data freshness: flag when upstream data sources stop updating within expected windows,
- log schema violations and type mismatches on incoming records.

Data-pipeline monitoring should trigger the same alert and incident workflows as model performance degradation.
