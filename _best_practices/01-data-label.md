---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Ensure Data Labelling is Performed in a Strictly Controlled Process
title: Ensure Data Labelling is Performed in a Strictly Controlled Process
category: Data
unique_id: data_lbl
index: 5
difficulty: "basic"
references: ["DLB", "DLML", "DCML", "DOML"]
comments: True
description:
image: #
photocredit: #

intent: Avoid invalid or incomplete labels. #
motivation: Controlling the data labelling process ensures label quality -- an important quality driver for supervised learning algorithms. #
applicability: Data label control should be applied to any ML application that uses labels, i.e. in supervised learning.
related: #
dependencies: #
survey_question: Q35
---

In supervised learning, labels are crucial for the proper functioning of any algorithm.
However, labelling large quantities of data is not trivial.
Incorrect labels introduce noise and may lead to sub-optimal results.
At first, data labelling raises challenges because the volume of data is typically large.
Secondly, choosing labels is a subjective activity and may introduce bias or noise.

Imposing a strictly controlled process for data labelling guarantees that your algorithm is served with the best data and helps to avoid later issues related to model debugging and error tracing.

A mature data labelling process includes peer-reviewing all labels by a second team member.

Lower or sub-optimal label quality can impact the whole ML pipeline.
In case this problem can not be addressed (and an ML solution is still desired), make sure you document and communicate this issue within the team.
