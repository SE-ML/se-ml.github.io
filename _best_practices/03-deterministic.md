---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Separate Deterministic and Probabilistic Concerns
title: Separate Deterministic and Probabilistic Concerns
category: Coding
unique_id: coding_deterministic
index: 30
difficulty: #
comments: True
references: [MLOPMAP]
description:
image: #
photocredit: #

intent: Reduce unnecessary probabilistic complexity by keeping deterministic logic out of ML models. #
motivation: Machine learning models introduce stochasticity, opacity, and latency. Applying them to problems that can be solved deterministically produces systems that are harder to test, debug, audit, and explain — without any benefit in quality. #
applicability: This principle applies to any system where ML components are designed or selected, and is especially important when integrating LLMs or generative models into larger applications.
related: [deployment_guardrails, deployment_verification, coding_build, efficient_compression, gov_inference_cost] #
dependencies: #
survey_question: #

labels: []

---

Not every problem in an ML system requires a machine learning solution. Using an ML model where a deterministic function would suffice adds cost, fragility, and opacity without benefit.

**Apply ML only where it is warranted**
ML is appropriate when the task requires pattern recognition, generalisation from examples, or handling genuine uncertainty in the input.
Use deterministic code — rules, formulas, look-up tables, constraint solvers — when:
- the output can be computed exactly from the input by a known procedure,
- correctness can be fully specified and tested without training data,
- the relationship between input and output does not change based on context or distribution.

Concrete examples of logic that should remain deterministic: input validation, currency conversion, date arithmetic, business rule enforcement, configuration-driven routing.

**Architect clean boundaries**
In systems that combine ML and deterministic logic, keep the two separated with explicit interfaces:
- pre-processing and post-processing pipelines that transform data should be deterministic and unit-tested independently of the model,
- the model's role should be limited to the inference step — producing a score, label, or generation — not to orchestrating control flow,
- downstream decisions that consume model output (e.g. thresholding, aggregation, business logic) should be implemented as deterministic code with explicit parameters, not embedded in the model.

This separation makes each component independently testable and replaceable, reduces inference cost by avoiding unnecessary model calls, and makes the system's behaviour easier to explain and audit.

**Validate the choice at design time**
When selecting an ML model for a new capability, explicitly ask: "Could this requirement be met with a deterministic implementation?" If yes, prefer the deterministic approach. If ML is chosen, document the justification.
