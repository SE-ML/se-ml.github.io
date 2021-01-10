---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Test all Feature Extraction Code
title: Test all Feature Extraction Code
category: Training
unique_id: exp_tstfeature
index: 11
difficulty: "advanced"
references: [CD4ML]
comments: True
description:
image: #
photocredit: #

intent: Avoid bugs in the feature extraction code. #
motivation: Many times a feature will merge two or more data attributes, or use custom data transformations. Testing custom feature extraction code ensures no errors or bugs are introduced in this process. #
applicability: The feature extraction code should be tested whenever features are manually  engineered (and not automatically extracted, e.g. through deep learning).
related: [data_sanity, coding_regr] #
dependencies: #
survey_question: Q40
---

Similar to <a href="/best_practices/01-sanity_check/"> applying sanity checks to external data sources</a>, it is important to check that data generated internally is consistent, and does not introduces errors or bugs.

In many cases, one would write custom code to merge data attributes into new features.
The code written for such operations needs to be unit-tested in order to ensure that it does not introduces functional bugs, but also to ensure that the returned data will match the expected values needed to train a machine learning algorithm.

Failing to test the feature extraction code may lead to unintended bugs with severe impact on the final model.
Such bugs are hard to detect and remove because they involve several data sources and functionality.

If automatically extracted features are used, they should be tested for correctness.