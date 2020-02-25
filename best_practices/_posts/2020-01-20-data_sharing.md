---
layout: practice
author: Alex Serban, Joost Visser
name: Make Data Sets Available on Shared Infrastructure (private or public)
category: Data
unique_id: data_share
index: 5
difficulty: "medium"
references: [SD4DL, MSCS, MMLP, PMLPP]
comments: True
description:
image: #
photocredit: #

intent: Avoid data duplication, data bottlenecks and heavy data transfer. #
motivation: The amount of data processed by ML models is higher than usual software systems, raising concerns related to duplication, transfer, storage and traceability. Making the data sets available on shared infrastructure helps mitigate these issues. #
applicability: #
related: #
dependencies: #
survey_question: Q36
---

Good data management and sharing is important for several reasons:
- access control,
- virtualization,
- versioning,
- maintainability and freshness,
- avoid duplication,
- avoid unnecessary transfers and save time.

Many applications deal with high data volumes.
Transferring or copying high data volumes is not trivial and may introduce large delays in the processing pipelines.
Needless to say duplication becomes an issue with large volumes of data.

Making data sets available on shared infrastructure (e.g. S3 Buckets or mountable disks) helps mitigate these issues.
Moreover, it facilitates the adoption of access control policies and provides traceability i.e. by keeping a data access log.