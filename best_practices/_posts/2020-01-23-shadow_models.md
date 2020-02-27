---
layout: practice
author: Alex Serban, Joost Visser
name: Enable Shadow Deployment
category: Deployment
unique_id: deployment_shadow
index: 22
difficulty: "medium"
references: [VML, MLLG, TFX]
comments: True
description:
image: #
photocredit: #

intent: Test a model's behavior on production data, without any impact on the service it provides. #
motivation: Before pushing a model into production, it is wise to test its quality and performance on data from production. In order to facilitate this task, one can deploy multiple models to 'shadow' each other. #
applicability: Shadow deployment should be implemented in any production-level ML application.
related: [deployment_automate] #
dependencies: #
survey_question: Q59
---

Instead of deploying a model straight into production, one can assess its quality and performance using the data from production without allowing the model to make final decisions.
This involves deploying the a model to "shadow" or "compete" with the model in production and redirect the data to both models.
The model that is already deployed will still handle all decisions, until the shadow model is assessed and promoted to production.

Using shadow models allows teams to avoid unintended behaviors in production  -- coming from skews between training and test data.
However, it introduces more complexity in the deployment infrastructure.
Luckily, <a href="https://github.com/SE-ML/awesome-seml#tooling" target="blank">tool support</a> for shadow or canary deployment is already matured.