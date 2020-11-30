---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Provide Audit Trails
category: Deployment
index: 34
unique_id: audit_trails
difficulty: na
references: [CAIAG, AIHLEG, TTAID] #
comments: True
description:
image: #
photocredit: #

intent: Allow post-mortem behaviour analysis of the application. #
motivation: Concerns about the social implications of ML and AI led to a rising interest to regulate and audit applications. #
applicability: Audit trails should be applied to any machine learning application.  #
related: [audits, deployment_log, interpretable] #
dependencies: Similarities, differences and connections to other practices #
survey_question: 1 #
survey_items: Our ML applications provide comprehensive audit trails that allow critical assessment of model behaviour.

---

The social implications that ML and more general AI technologies may have on the society call for tight regulations to ensure the consumer rights are respected. For example, the EU GDPR law, as well as the Credit score in the US, require the *right to an explanation* for automated decision making systems.

Post-mortem analysis and traceability of ML behaviour is difficult in case teams to not design the application for audit trails.
A first step towards opening the applications for audits is to devise a strategy for auditing and make it part of the development life-cycle.

Such a strategy should include plans for storing and preserving audit trails of past decisions, together with data describing each stage of the development life-cycle.
For example, define and store design checklists (which describe why a model was preferred over others), records about the training data distribution (at the time of developing a model), records regarding the known failures mode of the ML model and production logs that can trace back decisions to a model and the training data.

Automating the audit artifacts -- such as automatic generation of reports -- will enhance your ability to adhere to the audit strategy and will facilitate communication across teams.