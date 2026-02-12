---
layout: practice
author: András Schmelczer
name: Keep the Model and its Documentation Together
title: Keep the Model and its Documentation Together
category: Governance
unique_id: governance_model_card
index: 52
difficulty: na
references: [MCARD, MCMR2, MCT, GREATAI]
comments: True
description:
image:
photocredit:

intent: Models applied without a nuanced understanding of their capabilities and limits can easily lead to misuse.
motivation: Providing prospective users and/or the public with a clear description of the models' strengths, biases, and shortcomings must be an integral part of responsible open-sourcing. This way, both misguided applications and public distrust can be averted.
applicability: Clear documentation must be distributed together with the models in all cases where models are made accessible to third parties.
related: [data_lbl, team_communication, alert]
dependencies:
survey_question:

labels: [transparency]

---

ML models are not perfect, and their imperfections can often be unintuitive to notice and interpret. Therefore, it is expected of their creators to ensure that the model's users have a precise understanding of its boundaries. This includes measured performance, the means of measuring that &mdash; for instance, evaluation metrics and data used &mdash; applicability, and known edge cases.

Documentation can come in many shapes, but <a href="https://modelcards.withgoogle.com/about" target="_blank">Model Cards</a>, pioneered by Google, are a safe choice for starting out. They allow a large degree of freedom while still providing a clear structure.

Model cards and, in general, documentation of machine learning models should be aimed at both technical and non-technical audiences. It's not only for the engineers looking to apply it but also for the end-users whose data it might be applied to, and legal or other governing professionals who oversee the safety, legality, and ethics of the model's usage.
