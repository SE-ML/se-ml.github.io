---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Test for Social Bias in Training Data
category: Data
unique_id: social_bias
index: 3
difficulty: na
references: [ITDFDS, LFR, IFCUL, FMLSS] #
comments: True
description:
image: #
photocredit: #

intent: Identify instances of social bias in training data, in order to allow counteracting the effects of this bias in training and deployed models.
motivation: Bias in data is one of the main sources of unfairness in ML applications. Responsible use of ML requires that developers of ML applications counteract such unfairness, which starts with identifying the sources of bias. #
applicability: Testing for social bias in training data should be done whenever you work with input data that contains information that relates to people. Not only when your data has explicit fields for gender, ethnicity, etc, but also seemingly inocuous data like location, name, or even hobbies might implicitly encode social traits.  #
related: [discriminatory_attributes,subgroup_bias,risk] #
dependencies: Similarities, differences and connections to other practices #
survey_question: Q84 #
survey_item: We consistently test for social bias in our training data (regarding e.g. gender or ethnicity).
---

In order to avoid social bias in ML algorithms, it is imperative to *continuously* check that the training data is well balanced with respect to social attributes such as gender, or ethnicity.

In many cases, other data attributes (such as location or neighborhood) can be proxies to sensitive social attributes and may introduce latent bias.
Using or not testing for these latent biases is a common pitfall, called failure through unawareness. A common example is the one day delivery service offered by Amazon, which was biased for race: [Amazon Doesn’t Consider the Race of Its Customers. Should It?](https://www.bloomberg.com/graphics/2016-amazon-same-day/).

Social bias can be detected technically -- by analyising the distributions of social factors, and avoiding over or under representation.
However, technical limitations may prevent bias stemming from latent factors to be detected.


Therefore, it is important to be aware of technical limitations, and improve the social and human factors that can aid bias detection.
For example, in order to strengthen your teams' ability to detect and remove social biases, it is recommended to build diverse teams, both in terms of demographics and in terms of skillsets.