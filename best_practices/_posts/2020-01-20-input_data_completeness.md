---
layout: practice
author: Alex Serban, Joost Visser
name: Check Input Data for Completeness and Well Distributed
category: Data
id: data_complete
index: 2
difficulty: #
references: [DMP, MLTD, CTPML, DQML, MMLP]
comments: True
description: #
image: #
photocredit: #

intent: Avoid invalid or incomplete data being processed. #
motivation: The data generation processes are not static. Therefore, it is necessary to check that the data is still well distributed, complete and balanced. #
applicability: #
related: #
dependencies: #
survey_question: Q33
---

Besides performing <a href="/blog/2020/sanity_checks/">sanity checks</a> on the input data, it is recommended to constantly check for data evolution. In a constantly evolving envrironment, data will also evolve over time.
For example, your user distribution per geographical regions may change over time and may lead to futre biases towards an over-representative region.

Consider checking that:

- features are still present in enough examples,
- features have the right number of values (cardinality) (e.g. there can not be more than an age/age derived feature),
- hidden dependencies between data attributes are not present,
- the input data distribution did not shifted: e.g. a group is misrepresented.


Building a strong data check pipeline should also include
- dashboards or visual elements to continuously monitor data quality and
- alerts for informing team members when unusual events occur.

If your model performs close to real-time or online learning, a strong alert system can help to detect errors early and correct them.