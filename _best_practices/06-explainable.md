---
layout: practice
author:
name: Explain Results and Decisions to Users
category: Governance
index: 43
unique_id: explainable
difficulty: na
references: [AIHLEG] #
comments: True
description:
image: #
photocredit: #

intent: Allow users to critically assess the results and decisions of the ML application, so they can accept them on an informed basis, or catch possible errors.
motivation: Users are entitled to know the basis on which a decision that affects them was made. #
applicability: Explanations should be applied to any machine learning application.
related: [alert, audit_trails, interpretable, concerns]  #
dependencies: #
survey_question: Q101 #
survey_item: Our application provides each user with a clear explanation of the results or decisions that they receive.
---

ML systems involve highly complex between data, algorithms and models. As a result they are often difficult to understand, even for other experts.

In order to increase transparency and align the application with ethics guidelines, it is imperative to inform users on the reasons why a decision was made.
For example, the EU GDPR law, as well as the Credit score in the US, require the *right to an explanation* for automated decision making systems.

Not only may users be more accepting of decisions made by ML systems when they understand what the decision was based on, it also helps them to raise concerns when the explanation is unsatisfactory, or -- in the extreme case -- plain wrong. In turn this helps to improve ML systems to make better decisions, and provide improved explanations in the future.
