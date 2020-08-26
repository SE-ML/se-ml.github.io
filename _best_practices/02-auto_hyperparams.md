---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Automate Hyper-Parameter Optimisation
title: Automate Hyper-Parameter Optimisation
category: Training
unique_id: exp_hyperparam
index: 18
difficulty: "advanced"
comments: True
description:
image: #
photocredit: #

intent: Enhance experimentation, performnance and fair comparisons between algorithms, by automating hyper-parameter search and model selection. #
motivation: Finding the right hyper-parameters for a model or choosing between different ML models can be a daunting task. Automated methods to perform these activities are now available, with great 'off the shelf' tool support.  #
applicability: Automatic hyper-parameter optimisation should be considered in any ML application.
related: [exp_peer] #
dependencies: #
survey_question: Q80
---

The performance of ML models depends on the choice of hyper-parameters.
Moreover, in many cases one would train different ML models (e.g. SVMs or Gradient Boosting) and choose the better performing one.

Instead of manually trying out hyper-params or performing manual model selection, one can automate these tasks and gain experimentation speed and performance.

However, it is still recommended that models are peer-reviewed and assessed by team members before deployment to production.