---
layout: practice
author: Alex Serban, Joost Visser
name: Check that Input Data is Complete, Balanced and Well Distributed
category: Data
unique_id: data_complete
index: 2
difficulty: "advanced"
references: [DMP, MLTD, CTPML, DQML, MMLP]
comments: True
description: #
image: #
photocredit: #

intent: Avoid invalid or incomplete data being processed. #
motivation: The data generation processes are not static. Therefore, it is necessary to continuously check that data evolution does not introduce issues in distributions, completeness and balance. #
applicability: Data quality control should be applied to any machine learning application.
related: [data_sanity, deployment_distskew] #
dependencies: #
survey_question: Q33
---

Besides performing <a href="/blog/2020/sanity_checks/">sanity checks</a> on the input data, it is recommended to constantly check for data evolution. In a constantly evolving environment, data will also evolve over time.
For example, your user distribution per geographical regions may change with time and lead to future biases towards over-representative regions.

Continuously check that:

- features are still present in enough examples,
- features have the right number of values (cardinality) (e.g. there can not be more than an age/age derived feature),
- hidden dependencies between data attributes are not present,
- the input data distribution did not shifted: e.g. a group is misrepresented.


Many machine learning algorithms use the "independent and identically distributed" assumption, which means the training and test samples are independent (i.e. changing one sample does not influence the others) and are sampled from the *same* distribution.
In case your algorithms use this assumption, make sure to include checks between training, testing and production data to ensure no drifts are present.


Building a strong data validation pipeline should also include:
- dashboards or visual elements to continuously monitor data quality and
- alerts for informing team members when unusual events occur.

If your model performs close to real-time or online learning, a strong alert system can help to detect errors early and correct them.