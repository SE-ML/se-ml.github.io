---
layout: practice
author: Joost Visser, Alex Serban
name: Prevent Discriminatory Data Attributes Used As Model Features
category: Data
index: 6
unique_id: discriminatory_attributes
difficulty: na
references: [FMLSS] #
comments: True
description:
image: #
photocredit: #

intent: Avoid building discriminatory practices into ML applications. #
motivation: Using personal data attributes such as gender or ethnicity as features of ML algorithms introduces discriminatory bias, and ultimately leads to models with a negative impact on the society. #
applicability: Discriminatory attributes should not be used in applications with a direct or indirect impact on human lives, the society or the environment. #
related: [social_bias,subgroup_bias,risk] #
dependencies: #
survey_question: Q94 #
survey_item: We prevent potentially discriminatory data attributes (such as gender or ethnicity) from being used as model features.
---

When processing personal data -- for example the customer data in a banking application -- it is important to prevent discriminatory attributes from being used as model features, because the resulting models may base their decisions on these attributes, and ultimately introduce biases.

A widely known example for misusing this practice is the [COMPAS](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing) case; where discriminatory attributes were used to predict if a perpetrator was likely to recidivate.

An intuitive step to prevent such attributes from being used as feature is to remove them from the training data.
However, removing or not including sensitive attributes is no cure for fairness concerns, and can exacerbate them if used improperly.

Always be aware that latent sensitive attributes -- which can be revealed by a mix of features not considered discriminatory -- may be uncovered by ML algorithms, and ultimately have the same effect as using discriminatory attributes.

In order to prevent the use of discriminatory attributes, a hybrid approach is needed; consisting of removing the attributes from the training data, testing for latent factors that may uncover them, and constantly testing for other biases such as social or subgroup bias -- as indicated by the related practices.


