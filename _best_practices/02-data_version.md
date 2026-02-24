---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Versioning for Data, Model, Configurations and Training Scripts
title: Use Versioning for Data, Model, Configurations and Training Scripts
category: Training
unique_id: exp_versioning
index: 22
difficulty: "basic"
comments: True
references: [VML, MLPROD, MMLP, BPDL, MDLOPS, PMLPP, MGIT]
description:
image: #
photocredit: #

intent: Improve reproducibility, traceability and compliance. #
motivation: In order to reproduce previous machine learning experiments, one needs more than just the executable code. Versioning the training and testing data, the final model, and all configuration files is complementary to versioning the executable code. As ML systems grow to rely on fine-tuned foundation models and complex pipelines, tracking the full provenance and lineage of model artifacts becomes equally important. #
applicability: Versioning should be used in any machine learning application or experiment.
related: [exp_owner, exp_tstfeature, audit_trails, deployment_data_pipeline_feedback] #
dependencies: #
survey_question: Q48

labels: [traceability]

---
Versioning in machine learning involves more components than in traditional software: among the executable code we have to store the training and testing data sets, the configuration files and the final model artifacts.

Storing all information allows previous experiments to be reproduced and re-assessed.
Moreover, it helps auditing, compliance and backward traceability and compatibility.

However, many of these artifacts have distinct and large sizes, which makes versioning difficult.
In most cases, data and model artifacts will be versioned in different systems than code and configuration files.

In order to avoid versioning issues, make sure to:
- include a link to the data version in the code / configuration artifacts together with an unique id and a time stamp,
- add feature documentation for all data and link it to the code artifacts,
- add tests for data processing and merging,
- include scripts for running or deploying the experiment, e.g. bash scripts, infrastructure scripts, etc.

**Adopt consistent naming conventions for model artifacts**
As the number of trained models grows, ad-hoc naming quickly makes it impossible to trace which model is in production or how it was produced.
Establish and enforce a naming convention that encodes key metadata directly into the model identifier, for example:
`{project}-{task}-{architecture}-{dataset-version}-{date}-{run-id}`

Every model artifact should carry a unique identifier, a timestamp, and a link to the exact training configuration and data version that produced it.

**Track provenance and lineage explicitly**
For models derived from pre-trained or externally sourced foundation models — such as fine-tuned LLMs — lineage tracking must capture the full chain of custody:
- the source model identifier and version (including external checkpoints),
- the fine-tuning dataset and any data processing applied,
- intermediate checkpoints if multi-stage training was used.

This is particularly important for compliance and debugging: when a fine-tuned model misbehaves, tracing the issue requires knowing exactly which base model, data, and training decisions produced it.
Tools such as MGit and Git-Theta are specifically designed to version models at the parameter level and track this provenance across iterations.

**Evaluate model reuse before retraining**
Before triggering a full retraining run, check whether an existing model trained on a similar data distribution can be reused or fine-tuned instead.
This reduces compute cost and training time, and is only possible if models are versioned with sufficient metadata to assess their applicability to new tasks or distributions.

