---
layout: practice
author: András Schmelczer
name: Parallelise Feature Extraction
title: Parallelise Feature Extraction
category: Data
unique_id: data_parallel
index: 9
difficulty: na
comments: True
references: [RAY, PPP, GREATAI]
description:
image:
photocredit:

intent: Iterate quicker during feature engineering and be more predictable in production.
motivation: Before processing any data, features have to be extracted. Sometimes, this step can be computationally expensive, so speeding it up, for example, by parallelising the workload, can result in less time wasted during experimentation and a more predictable production deployment.
applicability: Parallelisation should be considered in machine learning applications where feature extraction is resource-intensive and efficiently parallelisable.
related: [exp_parallel] #
dependencies: #
survey_question:

labels: effectiveness

---

Depending on the maturity of the data engineering processes, in some cases, the researchers and engineers might end-up processing data solely using simple scripts. Correctness over performance might be reasonably prioritised in such a setup, leading to too much waiting around while the scripts run. This can slow down development and, if the same functions are deployed, even production inference.

Using a database with good support for online analytical processing (OLAP) use-cases (such as <a href="https://cassandra.apache.org/_/index.html" target="_blank">Apache Cassandra</a>) and building a proper, distributed processing cluster (using, for example, <a href="https://spark.apache.org/" target="_blank">Apache Spark</a>) are reasonable first steps for mitigating the issue. Of course, when the dataset is much smaller, single-machine processing can also be appropriate. But even in that case, keeping parallelisation in mind (achievable with, for instance, <a href="https://joblib.readthedocs.io/en/latest/" target="_blank">Joblib</a>) during experimentation is vital for rapid prototyping and increasing developer experience.

In some deployments where we have available unused resources, it can also make sense to parallelise the feature extraction of individual production inputs (given that it is efficiently doable). This can result in more predictable response times, which depend less on the input length.
