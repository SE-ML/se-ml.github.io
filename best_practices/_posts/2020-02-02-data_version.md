---
layout: practice
author: Alex Serban, Joost Visser
name: Use Versioning for Data, Model, Configurations and Training Scripts
title: Use Versioning for Data, Model, Configurations and Training Scripts
category: Experiment
unique_id: exp_versioning
index: 16
difficulty: "basic"
comments: True
references: [VML, MLPROD, MMLP, BPDL, MDLOPS, PMLPP]
description:
image: #
photocredit: #

intent: Improve reproducibility, traceability and compliance. #
motivation: In order to reproduce previous machine learning experiments, one needs more than just the executable code. Versioning the training and testing data, the final model and all configuration files concomitantly is complimentary to versioning the executable code. #
applicability: Versioning should be used in any ML application or experiment.
related: [exp_owner, exp_tstfeature] #
dependencies: #
survey_question: Q48
---

Versioning in machine learning learning involves more components than in traditional software: among the executable code we have to store the training and testing data sets, the configuration files and the final model artifacts.

Storing all information allows previous experiments to be reproduced and re-assessed.
Moreover, it helps auditing, compliance and backward traceability and compatibility.

However, many of these artifacts have distinct and large sizes, which makes versioning difficult.
In most cases data and model artifacts  will be versioned in different systems than code and configuration files.

In order to avoid versioning issues, make sure to:
- include a link to the data version in the code / configuration artifacts together with an unique id and a time stamp,
- add feature documentation for all data and link it to the code artifacts,
- add tests for data processing and merging,
- include scripts for running or deploying the experiment, e.g. bash scripts, infrastructure scripts, etc.

