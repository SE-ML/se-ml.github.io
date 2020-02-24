---
layout: practice
author: Alex Serban, Joost Visser
name: Ensure Data Labeling is Performed in a Strictly Controlled Process
category: Data
unique_id: data_lbl
index: 4
difficulty: #
references: ["DLB", "DLML", "DCML", "DOML"]
comments: True
description:
image: #
photocredit: #

intent: Avoid invalid or incomplete labels. #
motivation: Controlling the data labeling process ensures label quality -- an important quality factor for supervised learning algorithms. #
applicability: #
related: #
dependencies: #
survey_question: Q35
---

In supervised learning, labels are crucial for the well functioning of any algorithm.
However, labeling large quantities of data is not trivial.
Incorrect labels introduce noise and may lead to sub-optimal results.
At first, data labeling raises challenges because the volume of data is typically large.
Secondly, choosing labels is a subjective activity and may introduce bias or noise.

Imposing a strictly controlled process for data labeling guarantees that your algorithm is served with the best data and helps to avoid later issues related to model debugging and error tracing.