---
layout: practice
author: Alex Serban, Joost Visser
name: Use Versioning for Data, Model, Configurations and Training Scripts
category: Experiment
unique_id: exp_versioning
index: 16
difficulty: #
comments: True
references: [VML, MLPROD, MMLP, BPDL, MDLOPS, PMLPP]
description:
image: #
photocredit: #

intent: Improve reproducibility, traceability and compliance. #
motivation: In order to reproduce past machine learning experiments, we need more than just the executable code. Therefore, versioning the training and testing data, the final model and all configuration files concomitantly among the executable code is mandatory. #
applicability: #
related: #
dependencies: #
survey_question: Q48
---

Versioning in machine learning learning involves more components than in traditional software: among the executable code we have to store the training and testing data sets, the configuration files and the final model artifacts.

Storing all information allows past experiments to be reproduced and re-assessed.
Moreover,

Since many of these artifacts have distinct sizes, different versioning systems can be used for


- if data is versioned differently, make sure to include the data versioning link in the repo or vice-versa

Versioning and storing the data sets is very important for reproducibility and compliance purposes.