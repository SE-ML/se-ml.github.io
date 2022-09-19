---
layout: practice
author: András Schmelczer
name: Cache Production Predictions
title: Cache Production Predictions
category: Deployment
unique_id: deployment_cache
index: 39
difficulty: na
references: [SAASSA, GREEN, CMMD, GREATAI]
comments: True
description:
image:
photocredit:

intent: Improve performance, allow more flexibility for the clients, and reduce the deployment's carbon footprint.
motivation: Avoiding the expensive, especially in the case of Deep Learning models, recomputation of results can lead to lower latency, lower costs, and an overall more socially conscious deployment.
applicability: Caching should be implemented in production-level ML applications where repeating input values may occur.
related: [deployment_log]
dependencies:
survey_question:

labels: [quality]

---

Sustainability is an increasingly crucial concern of ethical AI, and avoiding wasting computing resources is a part of it. To this end, caching the results of expensive operations has to be considered in any ML deployment.

Caching is a well-known technique for improving the latency of repeated responses. By using it, we can avoid recomputing results that we have already calculated. However, extra care has to be taken in order not to expose private data to third parties; therefore, access control must be thoroughly considered. 

If the ML service's clients can rely on virtually instant responses to repeated queries, that can open up opportunities for different, new access patterns. This freedom can result in a developer friendlier API and better developer experience.
