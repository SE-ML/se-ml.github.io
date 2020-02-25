---
layout: practice
author: Alex Serban, Joost Visser
name: Test all Feature Extraction Code
category: Experiment
unique_id: exp_tstfeature
index: 8
difficulty: #
references: [CD4ML]
comments: True
description:
image: #
photocredit: #

intent: Avoid bugs in the feature extraction code. #
motivation: Many times a feature will merge two or more data attributes or use custom data transformations. Testing this custom feature extraction code ensures no errors or bugs are introduced in this process. #
applicability: #
related: [data_sanity, coding_regr] #
dependencies: #
survey_question: Q40
---

Similar to <a href="/blog/2020/sanity_checks/" target="blank">applying sanity checks to external data sources</a>, it is important to check that data generated internally is consistent and does not introduces errors or bugs.


In many cases, one would write custom code to merge data attributes into new features.
The code written for such operations needs to be unit-tested in order to ensure that it does not introduces functional bugs, but also to ensure that the returned data will match the expected values needed to train a ML algorithm.

Failing to test the feature extraction code may lead to unintended bugs with severe impact on the final model.
Such bugs are hard to debug and remove because they involve several data sources and functionality.

