---
layout: practice
author: András Schmelczer
name: Implement Standard Schemas for Common Prediction Tasks
title: Implement Standard Schemas for Common Prediction Tasks
category: Coding
unique_id: coding_schemas
index: 31
difficulty: na
references: [PYDANTIC, GREATAI]
comments: True
description:
image:
photocredit:

intent: Increase interoperability within the organisation and facilitate code reuse.
motivation: Developing tools, dashboards, and APIs for ML models can be made more efficient by allowing easily reusing them for different models.
applicability: All machine learning teams should share a repository of standard schemas within the organisation.
related: [data_reusable, team_communication, deployment_log]
dependencies:
survey_question:

labels: [agility, quality]

---

Standard prediction response schemas allow interchanging models without friction. They also enable agile teams to reuse their existing software support (such as dashboards and tools) across many different models implementing similar tasks. For example, multiclass classification tasks always result in a prediction, probability, and, optionally, an explanation. A multi-label classification task's result is often similar to a list of multiclass classification task results, etc.

Next to helping code reuse, quality can also be improved through this. For instance, having a required `explanation` field could coerce colleagues into considering more explainable approaches. 

Additionally, the mostly stable schemas can prevent the unnecessary overhead of deciding the appropriate schemas for each new ML service. It can also help avoid mistakes coming from small differences between inference function outputs, such as mistaking `log_probability` for a `probability` percentage.
