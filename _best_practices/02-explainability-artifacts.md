---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Produce Explainability Artifacts as First-Class Training Outputs
title: Produce Explainability Artifacts as First-Class Training Outputs
category: Training
unique_id: exp_explainability_artifacts
index: 25
difficulty: #
references: [XAIDESIGN, AIHLEG]
comments: True
description:
image: #
photocredit: #

intent: Make model behavior systematically understandable to developers, auditors, and stakeholders by generating explanation artifacts as a standard part of every training run. #
motivation: Explainability is often treated as a post-hoc concern, added after a model is built when needed. This makes it fragile, inconsistent, and disconnected from model evolution. Generating explanation artifacts during training ensures that every model version is accompanied by structured evidence of its behavior, supporting debugging, auditing, fairness assessment, and stakeholder communication. #
applicability: Applicable to any ML application where model behavior needs to be understood, justified, or audited, particularly in high-stakes domains or any system subject to regulation.
related: [interpretable, explainable, exp_versioning, exp_quality, gov_responsible] #
dependencies: #
survey_question: #

labels: []

---

Choosing an interpretable model (see [employ interpretable models](../02-interpretable/)) addresses explainability at the architecture level.
But even when interpretable models are not feasible, or when a black-box model is warranted by performance requirements, explanation artifacts can be systematically generated and versioned alongside model weights and metrics.

The goal is *explainability-by-design*: treating explanation outputs as a required, versioned artifact of the training pipeline rather than an optional inspection step.

#### Generate Standard Explanation Artifacts at Training Time
After each training run, produce and store the following as versioned outputs alongside the model:
- **Global feature importance plots**: summary charts (e.g. SHAP summary plots, permutation importance) showing which features drive predictions across the dataset,
- **Dependence plots**: visualizations of how model output changes as a function of individual features, revealing non-linearities and interactions,
- **Per-segment analysis**: feature importance breakdowns for key population subgroups, to surface differential behavior and support fairness assessment,
- **Example-based explanations**: representative correctly and incorrectly predicted instances with their local explanations (e.g. LIME or SHAP waterfall plots).

Store these alongside the model artifact so that every deployed version has an associated explanation snapshot.

#### Integrate Explanation Generation into the Training Pipeline
Explanation generation should be an automated step in the training pipeline, not a manual inspection task.
Treat a training run that produces no explanation artifacts as incomplete, the same way a run that produces no evaluation metrics would be.

#### Use Explanations for Debugging and Review
Explanation artifacts are not only for external stakeholders; they are a primary debugging tool.
When model quality drops, compare explanation artifacts across versions to identify which features changed in influence.
Peer review of models (see [peer review](../02-peer_review_mdl/)) should include review of explanation artifacts, not just performance metrics.

#### Version and Link Explanations to Model Releases
Explanation artifacts should be versioned together with the model and linked in the model registry (see [versioning](../02-data_version/)).
This ensures that when a model is rolled back or audited, the corresponding explanation snapshot is available without reconstruction.
