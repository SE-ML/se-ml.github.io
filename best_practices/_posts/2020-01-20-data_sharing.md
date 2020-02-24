---
layout: practice
author: Alex Serban, Joost Visser
name: Datasets are Available on Shared Infrastructure (private or public)
category: Data
unique_id: data_share
index: 5
difficulty: #
references: [SD4DL, MSCS, MMLP, PMLPP]
comments: True
description:
image: #
photocredit: #

intent: Avoid data duplication, data bottlenecks and heavy data transfer. #
motivation: The amount of input data for ML models is higher than usual software systems, demanding special practices to ensure good management. #
applicability: #
related: #
dependencies: #
survey_question: Q36
---

Good data management and sharing is important for several reasons:
- access control,
- virtualization,
- versioning,
- maintainainability and freshness.

Many applications deal with high data volumes.
Transfering or copying a high volume of data is not trivial.
Making datasets avaiable on shared infrastructuure (e.g. S3 Buckets, mountable disks) helps mitigate all these issues.
Moreover, it can provide tracebility.