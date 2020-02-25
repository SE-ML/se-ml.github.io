---
layout: practice
author: Alex Serban, Joost Visser
name: Enforce Fairness and Privacy
category: Governance
unique_id: gov_responsible
index: 50
difficulty: #
references: [DQML, MLFAIR, MLRES]
comments: True
description:
image: #
photocredit: #

intent: Avoid irresponsible use of machine learning and decisions with negative societal impact. #
motivation: When processing personal information or when developing decision making systems that can negatively impact individuals or groups, it is important to enforce requirements for fairness and privacy. #
applicability: #
related: [exp_status, deployment_monitor] #
dependencies: #
survey_question: Q64
---

Machine Learning is a data driven process and, in most cases, the algorithm's performance improves when using more data.
This characteristic of ML algorithms is a central drive for collecting and processing more data.
Although there are many benefits from processing personal and sensitive data, it is essential to consider and assess the potential privacy violations in using this data.


Moreover, if the ML model you are developing makes decisions about individuals that can have a negative impact on their life -- e.g. an automatic loan system that may automatically refuse loans -- it is crucial to assess the algorithm's fairness and inclusiveness for all members of the society.
Moreover, it is crucial to assess that decisions are based on clear and interpretable features.

Whenever processing personal information or whenever developing algorithms that take automated decisions, consider to:
- assess that the personal information does not implies privacy breaches,
- use privacy preserving ML whenever possible, e.g. differential privacy,
- define and implement metrics for bias, fairness and responsible use of ML,
- take security into account -- confidential information can be leaked by ML algorithms,
- continuously monitor that the algorithm behaves responsibly,
- be as transparent as possible about the data used and the model you are developing.

