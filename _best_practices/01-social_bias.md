---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Test for Social Bias in Training Data
category: Data
unique_id: social_bias
index: 3
difficulty: na
references: #
comments: True
description:
image: #
photocredit: #

intent: Identify instances of social bias in training data to allow counteracting the effects of this bias in training and deployed models
motivation: Bias in data is one of the main sources of unfairness in ML applications. Responsible use of ML requires that developers of ML applications counteract such unfairness, which starts with identifying the sources of bias. #
applicability: Testing for social bias in training data should be done whenever you work with input data that contains information that relates to people. Not only when your data has explicit fields for gender, ethnicity, etc, but also seemingly inocuous data like location, name, or even hobbies might implicitly encode social traits.  #
related: [discriminatory_attributes,subgroup_bias,risk] #
dependencies: Similarities, differences and connections to other practices #
survey_question: Q84 #
survey_item: We consistently test for social bias in our training data (regarding e.g. gender or ethnicity).
---


TODO
