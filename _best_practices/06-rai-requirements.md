---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Specify Responsible AI Requirements Before Development Begins
title: Specify Responsible AI Requirements Before Development Begins
category: Governance
unique_id: gov_rai_requirements
index: 48
difficulty: "medium"
references: [REMLRR, AIHLEG]
comments: True
description:
image: #
photocredit: #

intent: Surface ethical, fairness, and accountability constraints early, before design decisions make them costly to address. #
motivation: ML introduces unique requirements challenges — algorithm performance cannot be fully predicted upfront, and RAI concerns such as fairness, explainability, and privacy are difficult to specify as precise functional requirements. If not captured early, these constraints are discovered late, retrofitted awkwardly, or ignored entirely. #
applicability: Any ML application that processes personal data, makes decisions affecting individuals or groups, or operates in a regulated domain.
related: [gov_responsible, risk, social_bias, discriminatory_attributes, privacy_preserving, data_complete] #
dependencies: #
survey_question: #

labels: [EU]

---

Traditional requirements engineering techniques — interviews, focus groups, card sorting — remain valid for ML systems, but they need to be extended to capture the ethical and responsible AI (RAI) dimensions that ML introduces.
Because many RAI properties (e.g. degree of explainability, fairness across subgroups) are difficult to measure or predict before a model is trained, requirements must be treated as evolving artifacts, revisited iteratively throughout development rather than frozen at the start.

**Write ethical user stories**
Extend standard user stories to explicitly capture RAI expectations.
For each user-facing ML decision, ask: who could be harmed by a wrong prediction? What would a fair or explainable outcome look like for this user?
For example: *"As a loan applicant from a historically under-served group, I expect the model's decision to be explainable and free from proxy discrimination."*
These stories make implicit ethical assumptions visible and debatable before implementation begins.

**Develop RAI personas**
Alongside standard user personas, create personas that represent vulnerable, minority, or adversarially affected user groups.
RAI personas foreground how the system may fail specific populations and anchor fairness requirements to concrete human contexts rather than abstract metrics.
For example, a persona representing a non-native speaker in an automated hiring system surfaces requirements around language bias that a generic persona would miss.

**Define data requirements explicitly**
ML requirements are inseparable from data requirements.
Before collection begins, specify:
- the data volume and diversity needed to cover all relevant population subgroups,
- the data sources and their known limitations or biases,
- privacy and sensitivity constraints on what data may be collected and retained,
- the labeling protocol and acceptable sources of ground truth.

This prevents discovering fundamental data incompatibilities after significant collection effort.

**Embrace iterative refinement**
Accept that RAI requirements will be incomplete at the start.
As model behavior becomes observable during development, requirements should be revisited and updated.
Treat the initial specification as a hypothesis to be validated, not a contract to be executed.
Track changes to RAI requirements with the same rigor as changes to functional requirements.
