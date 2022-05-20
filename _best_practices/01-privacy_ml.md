---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Privacy-Preserving Machine Learning Techniques
category: Data
index: 7
unique_id: privacy_preserving
difficulty: "advanced"
references: [TTAID]
comments: True
description:
image: #
photocredit: #

intent: Provide privacy protection for individuals whose data is used in the development of machine learning applications. #
motivation: Many machine learning applications rely on personal data. As with other software applications, the user data should be handled with care, as stipulated by privacy regulations (e.g. GDPR), information security standards, and ethical criteria. Specifically for machine learning applications, privacy risk may occur because of pooling data from different sources, sharing data sets for training, or deploying models trained with personal data. Privacy-preserving techniques can be applied to mitigate these risks. #
applicability: Consider using privacy-preserving machine learning techniques whenever you are using data about individuals, especially in case of personally identifiable information. #
related: [gov_responsible] #
dependencies: #
survey_question: Q93 #
survey_item: We use privacy-preserving ML techniques (e.g. federated learning, differential privacy, or homomorphic encryption).

labels: [privacy]

---

Whenever processing data that can be used to identify or trace back information to individuals -- such as medical records -- it is imperative to use privacy preserving techniques in order to protect the individuals' privacy.
Moreover, machine learning models are known to leak information (see <a href="https://www.cs.cornell.edu/~shmat/shmat_oak17.pdf">membership attacks</a>), and may reveal crucial information about the training data.

Anonymisation, pseudonymisation, differential privacy, federated machine learning, or using cryptographic techniques -- such as homomorphic encryption -- are examples of privacy preserving machine learning techniques.

The tool support for privacy preserving machine learning is mature, with tools such as <a href="https://github.com/pytorch/opacus">Opacus</a>), <a href="https://github.com/facebookresearch/CrypTen">CrypTen</a> or <a href="https://github.com/OpenMined/PySyft">PySift</a> being developed and maintained by large research centres such as Facebook AI Research (FAIR).
