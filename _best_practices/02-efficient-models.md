---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use the Most Efficient Models and Optimise for Inference
title: Use the Most Efficient Models and Optimise for Inference
category: Training
index: 24
unique_id: efficient_compression
difficulty: "medium"
references: [DISTSV, MDLCMPRS] #
comments: True
description:
image: #
photocredit: #

intent: Avoid overparametrised or energy-inefficient models, and minimise computational cost across the full model lifecycle — from training to large-scale inference. #
motivation: Large models consume resources that are often excessive relative to the task. As models grow in size — particularly foundation models and LLMs — inefficiency compounds at inference time, where serving costs can exceed training costs. Applying efficiency strategies at every stage reduces development costs, operational expenses, energy consumption, and latency. #
applicability: Efficiency considerations should apply to any ML application, from small experiments to large-scale production systems serving many users.
related: [interpretable, exp_parallel, deployment_data_pipeline_feedback] #
dependencies: #
survey_question:  #
survey_item: #

labels: [robustness]

---

Large models are often associated with richer representations and better performance. 
However, the use of large models can lead to inefficient resource management.
For example, using smaller models which run at smaller resolutions for image classification tasks can potentially improve computational, storage and data transfer resources -- ultimately leading to smaller development and operational costs and to a smaller carbon footprint.
Therefore, the use of efficient models should be a critical objective in any application of ML.

There are multiple ways to select or develop efficient models, either by (i) selecting a model with less parameters for the task at hand or (ii) compressing, pruning or distilling a large model to a more efficient one.
The first strategy should always be tested, as thin models can bring more advantages -- e.g., better interpretability or faster run times.
For example, if a Random Forest model performs on par with a neural network, the former should always be employed.

The second strategy should be tested when only large models can be employed for the task at hand.
Compression, pruning or distillation are known strategies that can be used to significantly reduce the number of parameters of a model while also maintaining performance.

A third strategy addresses **inference-time optimisation**, which becomes critical when large models — particularly LLMs and foundation models — are served at scale.
At this scale, inference costs frequently exceed training costs, and efficiency gaps directly translate into financial and latency costs.
Consider the following techniques:
- **Quantization**: reduce numerical precision (e.g. from FP32 to INT8 or lower) to decrease memory footprint and increase throughput with minimal accuracy loss,
- **Kernel-level optimisation**: use hardware-aware implementations (e.g. FlashAttention, custom CUDA kernels) to reduce memory bandwidth bottlenecks during inference,
- **Speculative decoding and batching strategies**: improve throughput on autoregressive models by predicting multiple tokens in parallel or batching requests efficiently,
- **Cost-performance trade-off analysis**: explicitly measure the trade-off between model quality and inference cost for your deployment context — techniques like quantization or pruning can reduce costs but may degrade performance for specific user groups or tasks.

While leading organisations (e.g. DeepSeek, Mistral, OpenAI) already apply these techniques extensively, they remain underexplored in broader engineering practice.
Engineers should treat inference optimisation as a first-class engineering concern, not an afterthought.