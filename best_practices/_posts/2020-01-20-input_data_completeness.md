---
layout: practice
author: Alex Serban
name: Check Input Data for Completeness and Well Distributed
category: data_management
index: 2
difficulty: #
referenes: [DMP, MLTD, CTPML, DQML, MMLP]
comments: True
description: #
image: #
photocredit: #
---

Besides performing <a href="/blog/2020/sanity_checks/">sanity checks</a> on the input data, it is recommended to constantly check its evolution.

In an ever changing world, data will also evolve over time.

Consider checking that:

- features are still present in enough examples,
- features have the right number of values (cardinality) (e.g. there can not be more than an age / age derived feature),
- hidden dependencies between data attributes are not present,
- the input data distribution did not shifted: e.g. a group is misrepresented.


Building a strong data check pipeline should also include *visuals* or *dashboards* to continuously monitor data quality and raise *alerts* for unusual events.

If your model performs close to real-time or online learning, a strong alert system can help to detect errors early and correct them.