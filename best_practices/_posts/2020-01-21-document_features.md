---
layout: practice
author: Alex Serban, Joost Visser
name: Assign an Owner to Each Feature and Document its Rationale
category: Experiment
unique_id: exp_owner
index: 9
difficulty: "advanced"
comments: True
references: [Rs4ML]
description:
image: #
photocredit: #

intent: Enhance feature development, understanding and maintenance. #
motivation: In a large data set, with multiple features that are composed from various data attributes, it is hard to keep track and understand all features. By assigning an owner and documenting each feature, they become easier to maintain and comprehend. #
applicability: Features should have an owner and documentation whenever features are manually engineered (and not automatically extracted, e.g. through deep learning).
related: [exp_archive] #
dependencies: #
survey_question: Q39
---

Ensuring that someone in a team is in charge of the information regarding a feature facilitates feature maintainability and improves the overall understanding of the data and models.


Although feature names can be descriptive, it is important to also document their rationale in order to facilitate communication and share the knowledge among team members.


This practice assumes that whenever a feature owner is leaving a team, the ownership is transferred to other members.