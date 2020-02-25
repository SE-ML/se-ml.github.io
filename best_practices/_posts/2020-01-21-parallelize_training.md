---
layout: practice
author: Alex Serban, Joost Visser
name: Enable Parallel Training Experiments
category: Experiment
unique_id: exp_parallel
index: 12
difficulty: #
comments: True
references: [CD4ML, MLPROD]
description:
image: #
photocredit: #

intent: Avoid deadlocks during experimentation. #
motivation: Machine learning relies heavily on empirical processes. In order to allow fast experimentation and avoid deadlocks, it is recommended to think upfront of parallelization. #
applicability: #
related: #
dependencies: #
survey_question: Q43
---

Developing machine learning components is different than traditional software development because we expect that much of the code used during experimentation to be thrown away if the experiments failed.


This involves writing code that will be never used again, needless to say it will never reach production.


However, in order to enable fast experimentation and parallel deployment, the code must still be developed wisely.
Not using proper encapsulation or dependency management can significantly impact experiment parallelization and slow down the overall development.

% TODO: add more pointers?


