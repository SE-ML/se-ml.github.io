---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Design Hierarchical Fallback Architectures for Resilient ML Inference
title: Design Hierarchical Fallback Architectures for Resilient ML Inference
category: Deployment
unique_id: deployment_fallback
index: 49
difficulty: "advanced"
references: [HFAML]
comments: True
description:
image: #
photocredit: #

intent: Ensure ML systems degrade gracefully under uncertainty, failure, or out-of-distribution inputs rather than producing unreliable outputs. #
motivation: A deployed ML model will inevitably encounter inputs it cannot handle reliably — due to distribution shift, adversarial inputs, or edge cases not covered in training. Without a fallback strategy, these cases silently produce low-quality or harmful outputs. A hierarchical fallback architecture routes such cases to progressively safer alternatives, preserving system reliability without requiring a full rollback or manual intervention. #
applicability: Applicable to any production ML system operating in high-stakes or real-time contexts where model failures or low-confidence predictions carry non-trivial consequences.
related: [deployment_rollback, deployment_shadow, deployment_monitor, deployment_distskew, efficient_compression] #
dependencies: #
survey_question: #

labels: [robustness]

---

A hierarchical fallback architecture defines a cascade of models or strategies ordered from most capable to most reliable.
When the primary model cannot produce a trustworthy output, the system falls back to the next level — a simpler, more constrained, or more interpretable alternative — rather than propagating an unreliable prediction downstream.

This differs from [rollback](../04-rollback_models_prod/), which replaces a model across all future requests after detecting sustained degradation, and from [shadow deployment](../04-shadow_models_prod/), which tests a candidate model silently before promotion.
Hierarchical fallback operates *within a single request*, in real time, as a resilience mechanism.

**Design the fallback cascade**
Structure the cascade as a sequence of increasingly conservative alternatives:
1. **Primary model** — the full, highest-performance model (e.g. a large neural network or LLM), used when inputs are within the expected distribution and confidence is high,
2. **Intermediate fallback** — a simpler or more constrained model (e.g. a smaller model, a feature-reduced variant, or a fine-tuned version with tighter scope) used when the primary model signals uncertainty,
3. **Rule-based or deterministic fallback** — a hand-crafted decision layer or lookup that handles the most common or highest-stakes cases with guaranteed, auditable behavior,
4. **Abstention or human escalation** — when no automated layer can produce a reliable output, the system abstains or routes the case to a human reviewer rather than guessing.

**Define confidence-based routing criteria**
Each level transition should be triggered by an explicit, measurable condition:
- prediction confidence falling below a defined threshold,
- input features falling outside the training distribution (out-of-distribution detection),
- output violating a known constraint (e.g. a physically impossible value, a policy-violating response).

Routing logic should be implemented in traditional software, not delegated to the model itself, to ensure deterministic and auditable behavior.

**Log all fallback events**
Every fallback activation is a diagnostic signal.
Log the triggering condition, the level activated, and the output produced.
Monitor fallback rates over time — a rising rate indicates the primary model is drifting and the [automated retraining pipeline](../04-data-pipeline-feedback/) should be engaged.

**Keep fallback layers tested and maintained**
Fallback layers are production code and carry production risk.
They should be subject to the same testing, versioning, and review practices as the primary model.
An untested fallback that activates under pressure is worse than no fallback at all.
