---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use The Most Efficient Models
category: Training
index: 24
unique_id: efficient_compression
difficulty: na
references: [DISTSV, ] #
comments: True
description:
image: #
photocredit: #

intent: Avoid overparametrised or energy-inefficient models. #
motivation: Overparametrised or large models consume resources that are potentially excessive. Using smaller models -- such as pruned, compressed or distilled models -- can often make efficient use of computational resources without loss of performance.
applicability: Efficient models should be the first choice for any ML application.
related: [] #
dependencies: #
survey_question:  #
survey_item: # 


# labels: [agency]

---

Large models are often associated with richer representations and better performance. 
However, the use of large models can lead to inefficient resource management.
For example, using smaller models which run at smaller resolutions for image classification tasks can potentially improve computational, storage and data transfer resources -- ultimately leading to smaller development and operational costs and to a smaller carbon footprint.
Therefore, the use of efficient models should be a critical objective in any application of ML.

There are multiple ways to select or develop efficient models, either by (i) selecting a model with less parameters for the task at hand or (ii) compressing, pruning or distilling a large model to a more efficient one.
The first strategy should always be tested, as thin models can bring more advantages -- e.g., better interpretability or faster run times.
For example, if a Random Forest model performs on par with a neural network, the former should always be employed.

The second strategy should be tested when only large models can be employed for the task at hand.
Compression, pruning or distillation are known strategy that can be used to significantly reduce the number of parameters of a model while also maintaining performance.