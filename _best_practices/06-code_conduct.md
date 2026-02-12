---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Establish Responsible AI Values
category: Governance
index: 45
difficulty: "advanced"
references: [TTAID, AIHLEG] #
comments: True
description:
image: #
photocredit: #

#intent: Build trust and ensure adherence to ethical principles and values. #
#intent: Make explicit to all stakeholders what the objectives and constraints of your ML application are #
intent: Explicitly align all stakeholders on the ethical values and constraints of your machine learning application
#motivation: ML and AI can severly impact human lives, usually without  malicious intentions.   #
#motivation: By setting explicit goverance objectives, all stakeholders can align on the constraints and goals that the team and their product can be held accountable for. #
motivation: Machine learning applications can severely impact human lives. Avoiding negative impacts, even without malicious intent, requires all stakeholders to operate according to the same ethical values.
#applicability: Code of conducts should be applied to any machine learning application. #
#applicability: Governance objectives should be set for any production-level ML application.
applicability: Values for Responsible AI should be established for any ML application.
related: [tradeoff,audits,interpretable] #
dependencies: #
survey_question: Q99 #
survey_item: Our organisation subscribes to a code of conduct for Responsible AI.

labels: [transparency]

---

A good starting point for sharing ethical values across organisations is to subscribe to a code of conduct. You can create one specific for your situation, or you can refer to a general governance framework.

General governance frameworks that you may want to refer to include:
- <a href="https://ai.google/responsibilities/responsible-ai-practices">Google Responsible AI</a>
- <a href="https://www.microsoft.com/en-us/ai/responsible-ai">Microsoft AI principles</a>
- <a href="https://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai">European Commission High-Level Expert Group - Ethical guidelines for trustworthy AI</a>

These frameworks set high-level objectives for concerns such as security, privacy, and fairness. They can be complemented or refined for your specific situation.

Defining or subscribing to a code of conduct helps to build trust with users and enhances the auditability of your development process and your applications.

The values set by a code of conduct can be refined into a set of concrete governance objectives.
The governance objectives appropriate for a given machine learning application depend on factors such as:
- the type of **data** being processed: for example, when personal information is processed, privacy objectives are relevant
- the **usage** context: for example, when used for autonomous driving, safety objectives are relevant
- the **organisational** context: for example, a government agency may require usage of open data and non-proprietary machine learning algorithms

