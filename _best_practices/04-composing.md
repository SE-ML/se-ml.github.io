---
layout: practice
author: András Schmelczer
name: Allow Robustly Composing Inference Functions
title: Allow Robustly Composing Inference Functions
category: Deployment
unique_id: deployment_composing
index: 40
difficulty: na
references: [MSCS, GREATAI]
comments: True
description:
image:
photocredit:

intent: Create simpler services and promote reuse by letting the inference functions call each other.
motivation: Just as in conventional software, composability and modularity can lead to simpler and more flexible architectures. However, extra care needs to be taken to avoid non-monotonic error propagation. 
applicability: Enabling robust inference function composition should be implemented in any production-level ML application.
related: [exp_versioning, governance_model_card]
dependencies:
survey_question:

labels: [quality, agility]

---

Letting inference functions call each other can lead to more flexibility and, in many cases, better performance because each core functionality has to be implemented only once. Therefore, more resources can be committed to improving their quality, and the knowledge doesn't need to be scattered around a multitude of models. 

However, extra attention must be given to the proper documentation of reusable models and their versions. The intertwined nature of many ML services may lead to non-monotonic error propagation, meaning that improvements in one part of the system might decrease the overall system quality. So, allowing pinning down model versions across the entire call tree and/or robust testing should be in place in order to mitigate this.

Additionally, even though most inference functions are CPU-bound (or GPU-bound), they can end up being IO-bound if they rely on the results of other remote services. This gives an opportunity to a significant performance (throughput) improvement, which can be achieved by implementing inference functions in an <a href="https://docs.python.org/3/library/asyncio-task.html" target="_blank">asynchronous manner</a>.
