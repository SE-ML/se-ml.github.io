---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Employ Interpretable Models When Possible
category: Training
index: 14
unique_id: interpretable
difficulty: na
references: [IMLG,TTAID,AIHLEG] #
comments: True
description:
image: #
photocredit: #

intent: Interpretable models help users, developers, and auditors to understand and account for the results of machine learning applications. #
motivation: Interpretable models help to build trust, transparency and auditability of machine learning applications. Moreover, they help application developers to understand the decisions, learn more about the problems solved, and understand the data.  #
applicability: Non-interpretable models often only provide a performance gain over interpretable alternatives. Whenever possible, it is recommended to use interpretable models over non-interpretable, black-box models even though small performance benefits are sacrificed. #
related: [tradeoff, alert] #
dependencies: #
survey_question: Q104 #
survey_item: Our ML applications employ interpretable models whenever possible.

---

In machine learning applications, developers are often faced with a trade-off between understanding *why* a decision is made, and focusing solely on performance metrics.
In many cases, knowing *why* can help to learn more about the problem solved, the data and the reasons why an algorithm fails.

In some scenarios, failures of ML models may not have major consequences.
For example, a recommender system for e-commerce can fail to provide the intended predictions without impacting human lives.
Nevertheless, understanding the failures modes of the system can help developers to rapidly solve the issues, and provide a better service.

In other scenarios, such as using deep learning for object recognition, non-interpretable models offer significant performance advantages over interpretable models.
Balancing the trade-off between black-box models and more interpretable ones is a task ML developers will face all the time.
However, whenever an interpretable model offers competitive performance with black-box models, it is recommended to use the former.
