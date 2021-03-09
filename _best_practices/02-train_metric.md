---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Capture the Training Objective in a Metric that is Easy to Measure and Understand
title: Capture the Training Objective in a Metric that is Easy to Measure and Understand
category: Training
unique_id: exp_trainingmetric
index: 10
difficulty: "basic"
references: [Rs4ML, OPML, DSTEAM, MLTEAM]
comments: True
description:
image: #
photocredit: #

intent: Ensure the machine learning objective is easy to measure and it is a good proxy for the <i>true</i> objective. #
motivation: Many times the <i>true</i> objective is hard to capture in a metric, and may lead to entangled measurements. Choosing a simple, observable metric as a proxy simplifies things, leads to better interpretability, and enhances communication within the team. #
applicability: All training objectives should be captured in an easy to comprehend metric.
related: [exp_trainingobjective] #
dependencies: #
survey_question: Q38

labels:

---

Choosing an objective to optimize is not trivial because (1) the objective may be hard to capture in a metric, and (2) the objective evolves over time.


In both cases, over-engineering a metric may lead to entangled measurements, which are hard to comprehend or assess.


Simple metrics, that are easy to measure and comprehend are considered better proxies for the true objective of a machine learning application.
Working together with business or data analysts to ensure the metrics reflect business values helps to align the measurements with the true objective.


A great example can be found in <a href="https://developers.google.com/machine-learning/guides/rules-of-ml">the 13th rule for machine learning</a> by Martin Zinchevich.