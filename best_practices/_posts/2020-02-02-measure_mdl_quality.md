---
layout: practice
author: Alex Serban, Joost Visser
name: Continuously Measure Model Quality and Performance
title: Continuously Measure Model Quality and Performance
category: Experiment
unique_id: exp_quality
index: 14
difficulty: "basic"
references: [Rs4ML, TDBML]
comments: True
description:
image: #
photocredit: #

intent: Detect errors early and improve experimentation agility. #
motivation: #
applicability: Quality monitoring should be used in any training experiment.
related: [exp_status, deployment_monitor] #
dependencies: #
survey_question: Q44
---

For long running experiments -- such as training deep neural networks for object recognition or language tasks -- it is important to detect errors as early as possible in the training process.
Moreover, it is important to continuously check model quality and performance on different benchmarks which reflect as good as possible the production environment.

By continuously monitoring the model's quality and performance, one allows errors to be detected and contained early.
Moreover, experiments can be stopped early, avoiding futile use of resources.

Ultimately, continuous monitoring enhances experimentation agility.
It also helps to keep an experiment "log-book" and keep track of past experiments and hyper-params configuration.

Monitoring should also include regular snapshots of the model in order to return to different versions of the model and facilitate retraining.