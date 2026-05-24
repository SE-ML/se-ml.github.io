---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Apply Layered Guardrails to ML System Behaviour
title: Apply Layered Guardrails to ML System Behaviour
category: Deployment
unique_id: deployment_guardrails
index: 42
difficulty: #
comments: True
references: [HFAML, ISO42001, RAIPCAT]
description:
image: #
photocredit: #

intent: Constrain the space of possible ML system behaviours and limit blast radius of failures. #
motivation: ML models are probabilistic and can produce outputs that are unexpected, unsafe, or policy-violating. Unlike traditional software, these failures are not easily prevented at development time. Layered guardrails bound what the system is allowed to do at runtime, independently of what the model predicts. #
applicability: Guardrails should be applied to any ML system whose outputs are consequential, including autonomous actions, user-facing content, financial decisions, or safety-critical inference.
related: [deployment_fallback, deployment_rollback, deployment_monitor, deployment_verification, coding_deterministic, gov_rai_governance] #
dependencies: #
survey_question: #

labels: []

---

No ML model can guarantee its outputs are always safe, appropriate, or within policy. Guardrails are independent mechanisms, separate from the model itself, that enforce constraints on system behaviour at runtime.

Design guardrails in layers so that multiple independent checks must all fail before a harmful outcome escapes:

#### Input Guardrails
Validate and sanitise inputs before they reach the model:
- enforce schema, type, and range constraints on incoming data,
- detect malformed, adversarial, or out-of-distribution inputs and reject or flag them,
- apply content filtering or access control checks before invoking the model.

#### Output Guardrails
Validate model outputs before they are acted on or surfaced to users:
- check that outputs conform to expected format, vocabulary, or value range,
- apply policy rules that the model cannot be trusted to enforce itself (e.g. prohibited content, regulatory constraints),
- route low-confidence or out-of-distribution outputs to a fallback or human review rather than acting on them.

#### Operational Guardrails
Protect the system from runaway or degraded operation:
- apply bounded retry logic: retries on transient failures must have a maximum attempt count and exponential backoff to prevent feedback loops,
- implement timeouts at every model call site; never allow an unbounded wait,
- use circuit breakers to stop issuing model calls when error rates exceed a threshold, and recover gracefully.

#### Governance Guardrails
At design time, enumerate the constraints the system must respect and encode each as an explicit, testable guardrail. Treat any guardrail violation surfaced in production as an incident with a root-cause analysis, not just a handled exception.
