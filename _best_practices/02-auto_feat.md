---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Automated Feature Generation and Selection
category: Training #
unique_id: exp_auto_feat
index: 17
difficulty: "advanced"
references: #
comments: True
description:
image: #
photocredit: #

intent: Reduce human effort required to develop and select features through automation #
motivation: Developing high-quality features, and identifying which feature combinations are most useful is a time consuming task. While human validation is still needed for automatically generated or selected features, it can greatly reduce the total required effort. #
applicability: Automated feature generation and selection is useful in any ML application where features are used, as long as the expertise is available to assess the quality of what is generated. #
related: [exp_owner] #
dependencies: #
survey_question: Q90 #
---

Creating high quality features is complex and time-consuming. By automating this process it is possible to find better features, and especially to reduce the human time needed for this task. Similarly, a subset of features can be selected automatically. This reduces the need for manual experimentation with different combinations of features.

Automation is not magic, and careful selection and monitoring of for instance the performance metrics used for feature generation remain important.

Another point is that generated features might exacerbate biases in the data because it may improve performance on the training data. It might also take advantage of biases that are not immediately obvious when looking at the data, and thus may have been left in. While these issues also exist in manual feature generation and selection, special care needs to be taken to not blindly trust an automated system. The automatically generated and selected features need to be assessed with the same care as any other feature. To aid this process, automatically generated features should have an owner and documentation, just like manually created features (see related practices).
