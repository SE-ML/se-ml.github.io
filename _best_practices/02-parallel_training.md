---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Enable Parallel Training Experiments
title: Enable Parallel Training Experiments
category: Training
unique_id: exp_parallel
index: 17
difficulty: "basic"
comments: True
references: [CD4ML, MLPROD]
description:
image: #
photocredit: #

intent: Avoid deadlocks during experimentation. #
motivation: Machine learning relies heavily on empirical processes. In order to allow fast experimentation and avoid deadlocks, it is recommended to think upfront of experiment parallelisation. #
applicability: Parallelisation should be considered in any machine learning application.
related: [exp_status] #
dependencies: #
survey_question: Q43

labels: agility

---

The development of machine learning components is different than traditional software development because we expect that much of the code used during experimentation to be thrown away when the experiments failed.


This involves writing code that will be never used again, needless to say it will never reach production.


However, in order to enable fast experimentation and parallel deployment, the code must still be developed and managed wisely.
Not using proper encapsulation or dependency management can significantly impact experiment parallelisation, and slow down development.


In order to ease parallelisation, make sure to:
- think of and prepare the infrastructure for parallel processing and deployment,
- encapsulate code,
- avoid hidden dependencies


and use virtualization, e.g. <a href="https://www.docker.com/">Docker</a>.


