---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Provide Audit Trails
category: Deployment
index: 38
unique_id: audit_trails
difficulty: "advanced"
references: [CAIAG, AIHLEG, TTAID] #
comments: True
description:
image: #
photocredit: #

intent: Allow post-mortem behaviour analysis of the application. #
motivation: Concerns about the social implications of machine learning and artificial intelligence led to a rising interest to regulate and audit applications. #
applicability: Audit trails should be applied to any machine learning application.  #
related: [audits, deployment_log, interpretable] #
dependencies: #
survey_question: Q96 #
survey_items: Our ML applications provide comprehensive audit trails that allow critical assessment of model behaviour.


labels: [accountability]

---

The social implications that machine learning and more general artificial intelligence technologies may have on society call for tight regulations to ensure the consumer rights are respected. For example, the EU GDPR law, as well as the Credit score in the US, require the *right to an explanation* for automated decision making systems.

Post-mortem analysis and traceability of model behaviour is difficult in case teams do not design the application for audit trails.
A first step towards opening the applications for audits is to devise a strategy for auditing and make it part of the development life-cycle.

Such a strategy should include plans for storing and preserving audit trails of past decisions, together with data describing each stage of the development life-cycle.
For example, define and store design checklists (which describe why a model was preferred over others), keep records about the training data distribution (at the time of developing a model), keep records regarding the known failure modes of the model, and keep production logs that can trace back decisions to a model and the used training data.

Automating the audit artefacts -- such as automatic generation of reports -- will enhance your ability to adhere to the audit strategy and will facilitate communication across teams.
