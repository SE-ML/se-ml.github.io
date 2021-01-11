---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Make Data Sets Available on Shared Infrastructure (private or public)
title: Make Data Sets Available on Shared Infrastructure (private or public)
category: Data
unique_id: data_share
index: 8
difficulty: "medium"
references: [SD4DL, MSCS, MMLP, PMLPP]
comments: True
description:
image: #
photocredit: #

intent: Avoid data duplication, data bottlenecks, or unnecessary transfer of large data sets. #
motivation: The amount of data processed by machine learning models is higher than usual software systems, raising concerns related to duplication, transfer, storage, and traceability. Making the data sets available on shared infrastructure helps mitigate these issues. #
applicability: Data availability on shared infrastructure should be applied to any machine learning application.
related: #
dependencies: #
survey_question: Q36
---

Good data management and storage is important for several reasons:
- access control,
- virtualisation,
- versioning,
- maintainability and freshness,
- to avoid duplication,
- to avoid unnecessary transfers, and save time.

Many applications deal with large data volumes.
Transferring (or copying) large data volumes is not trivial, and may introduce delays in the processing pipelines.
Needless to say duplication becomes an issue with large volumes of data.

Making data sets available on shared infrastructure (e.g. S3 Buckets or mountable disks) helps mitigate these issues.
Moreover, it facilitates the adoption of access control policies, and provides traceability i.e. by keeping a data access log.

Adopting standard naming conventions for the data sets -- e.g. to reflect the version -- is also considered a best practice.
