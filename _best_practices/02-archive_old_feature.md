---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Actively Remove or Archive Features That are Not Used
title: Actively Remove or Archive Features That are Not Used
category: Training
unique_id: exp_archive
index: 14
difficulty: "medium"
comments: True
references: [Rs4ML, MLTD]
description:
image: #
photocredit: #

intent: Avoid technical debt caused by unused features. #
motivation: Features that are no longer used introduce technical debt and clutter. Removing or cleaning unused features from the data pipeline helps concentrate only on promising features, and improves understandability and maintenance.  #
applicability: Features should be archived whenever features are manually engineered (and not automatically extracted, e.g. through deep learning).
related: [data_complete, exp_owner] #
dependencies: #
survey_question: Q41

labels: quality
---

When features which are no longer used are not removed, they introduce clutter in the processing pipeline.


This is equivalent to not removing *dead code* in traditional programming.


Keeping the pipeline clean from unused features allows faster experimentation and result interpretation, by focusing only on the most relevant features.
It also improves debugging.


When removing features, it is also important to consider coverage: if some features are only rarely present, they are good candidates for removal.


If you opt to not remove unused features, make sure that their documentation reflects this status.