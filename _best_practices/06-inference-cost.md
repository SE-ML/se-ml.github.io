---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Track and Govern AI Inference Costs
title: Track and Govern AI Inference Costs
category: Governance
unique_id: gov_inference_cost
index: 54
difficulty: "medium"
comments: True
references: [MLOPMAP]
description:
image: #
photocredit: #

intent: Prevent uncontrolled AI inference spend and make cost a first-class engineering concern. #
motivation: Serving large models — especially LLM APIs or GPU-based deep learning — can generate costs that are invisible until they appear on a cloud bill. Without instrumentation and governance, teams cannot make informed trade-offs between model quality, latency, and cost. #
applicability: Cost tracking and governance should be applied to any ML system served at scale or relying on pay-per-use APIs.
related: [efficient_compression, deployment_monitor, deployment_observability, gov_rai_governance] #
dependencies: #
survey_question: #

labels: [sustainability, traceability]

---

As machine learning systems move into production, inference cost can quickly dominate the total system cost — particularly for large language models accessed via APIs or GPU-intensive deep learning workloads.

**Instrument and attribute costs**
Measure and log the compute cost of every inference request, broken down by model, endpoint, and use case.
For API-based models, record token usage per call and aggregate by feature or user segment.
For self-hosted models, track GPU/CPU utilisation, memory, and infrastructure spend per deployment.
Cost instrumentation should be part of the same observability stack as latency and quality metrics.

**Set budgets and alerts**
Define cost budgets per model and per team, and configure alerts when spending approaches thresholds.
Treat unexpected cost spikes as incidents: investigate whether they are caused by traffic growth, model changes, or inefficient prompting patterns.

**Make cost a design-time trade-off**
Before deploying a model, explicitly evaluate the cost-quality trade-off:
- benchmark lighter models or quantised variants against the target quality bar — if the cheaper model is sufficient, use it,
- evaluate batching, caching, and request coalescing strategies at design time rather than as afterthoughts,
- document the cost assumptions for the selected model in the deployment decision record.

**Govern API usage**
For third-party LLM APIs, apply rate limits and quotas at the application level to protect against runaway loops or misbehaving clients.
Review and renegotiate API contracts as usage scales.
Avoid hard-coding specific external model versions without a plan for cost reassessment when pricing changes.
