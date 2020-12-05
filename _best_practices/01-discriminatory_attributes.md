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
motivation: Using personal data attributes such as gender or ethnicity as features of ML algorithms introduces discriminatory bias, and ultimately leads to models with a negative impact on society. #
applicability: Discriminatory attributes should not be used in applications with a direct or indirect impact on human lives, society or the environment. #
related: [social_bias,subgroup_bias,risk] #
dependencies: #
survey_question: Q94 #
survey_item: We prevent potentially discriminatory data attributes (such as gender or ethnicity) from being used as model features.
---

When processing personal data -- for example the customer data in a banking application -- it is important to prevent discriminatory attributes from being used as model features, because the resulting models may base their decisions on these attributes, and ultimately introduce biases.

A widely known example for misusing this practice is the <a href="https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing">COMPAS</a> case; where discriminatory attributes were used to predict if a perpetrator was likely to recidivate.

An intuitive step to prevent such attributes from being used as feature is to remove them from the training data.
However, removing sensitive attributes (or not including them in the first place) is no cure for fairness concerns, and can exacerbate them if used improperly.

Always be aware that there may be latent sensivtive attributes. For instance, sometimes a combination of features -- that are not considered discriminatory themselves -- can be used by an ML algorithm to reconstruct a discriminatory attribute. Ultimately, this would have the same effect as using discriminatory attributes directly.

In order to prevent the use of discriminatory attributes, a hybrid approach is needed; consisting of removing the attributes from the training data, testing for latent factors that may uncover them, and constantly testing for other biases such as <a href="/best_practices/01-social_bias/">social</a> or <a href="/best_practices/02-subgroup_bias/"></a> bias.


