---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Log Production Predictions with the Model's Version and Input Data
title: Log Production Predictions with the Model's Version and Input Data
category: Deployment
unique_id: deployment_log
index: 33
difficulty: "advanced"
references: [MMLP, MLGov, MDLOPS]
comments: True
description:
image: #
photocredit: #

intent: Enhance debugging, enable traceability, reproducibility, compliance and incident management. #
motivation: Tracing decisions back to the input data and the model's version can be difficult. It is therefore recommended to log production predictions together with the model's version and input data.  #
applicability: Prediction logging should be implemented in any production-level ML application.
related: [exp_versioning]
dependencies: #
survey_question: Q63
---

Debugging production models is difficult if one does not have access to the input data.
Moreover, tracing decisions and mitigating incidents without access to the input data is almost inconceivable.

In order to mitigate these issues, but also enhance traceability, it is recommended to log production prediction together with the model's version and input data.

If <a href="/blog/2020/data_version/" target="blank">model and data versioning</a> is done properly, the model's version will lead to the training data repository and enable complete reproducibility.