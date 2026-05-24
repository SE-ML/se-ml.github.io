---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Check that Input Data is Complete, Balanced and Well Distributed
title: Check that Input Data is Complete, Balanced and Well Distributed
category: Data
unique_id: data_complete
index: 2
difficulty: "basic"
references: [DMP, MLTD, CTPML, MMLP, DQAML]
comments: True
description: #
image: #
photocredit: #

intent: Avoid invalid or incomplete data being processed. #
motivation: The data generation processes are not static. Therefore, it is necessary to continuously check that data evolution does not introduce issues in distributions, completeness and balance. Beyond distributional checks, recurring data quality anti-patterns, such as structural issues with schema, labels, or feature ratios, can silently degrade model performance if not systematically detected. #
applicability: Data quality control should be applied to any machine learning application.
related: [data_sanity, data_lbl, deployment_distskew, social_bias] #
dependencies: #
survey_question: Q33

labels:

---

Besides performing <a href="/best_practices/01-sanity_check/">sanity checks</a> on the input data, it is recommended to constantly check for data evolution. In a continuously evolving environment, the data distribution will evolve over time.
For example, your user distribution per geographical regions may change with time, and lead to future biases towards over-representative regions.

Continuously check that:

- features are still present in enough examples,
- features have the right number of values (cardinality) (e.g. there can not be more than one age/age derived feature),
- hidden dependencies between data attributes are not present,
- the input data distribution did not shift: e.g. a group is under- or over-represented.


Many machine learning algorithms use the "independent and identically distributed" assumption, which states that training and test samples are independent (i.e. changing one sample does not influence the others) and are sampled from the *same* distribution.
In case your algorithms use this assumption, make sure to include checks between training, testing and production data to ensure no distribution drifts are present.


Building a strong data validation pipeline should also include:
- dashboards or visual elements to continuously monitor data quality, and
- alerts that inform team members when unusual events occur.

If your model performs close to real-time, or online learning, a strong alert system can help to detect errors early and correct them.

#### Watch for Common Data Quality Anti-Patterns
Beyond distribution drift, a number of recurring structural anti-patterns can silently degrade model quality and are frequently overlooked:
- **Missing values**: check for unexpected nulls or placeholder values (e.g. -1, "unknown") that encode missingness implicitly rather than explicitly,
- **Schema violations**: validate that column types, value ranges, and categorical vocabularies remain consistent across data batches and sources,
- **Imbalanced class distributions**: check that the ratio of positive to negative labels (or across multi-class targets) is within acceptable bounds; severe imbalance can mislead standard metrics,
- **Label overlaps or inconsistencies**: detect cases where the same or near-identical inputs carry conflicting labels, often introduced by different annotators or labeling policy changes,
- **Poor feature-to-sample ratio**: for tabular data, verify that the number of rows is sufficiently large relative to the number of features; a low ratio increases the risk of overfitting and instability.

These checks should be automated and run as part of the data validation pipeline, with failures treated as blocking issues before data enters training.