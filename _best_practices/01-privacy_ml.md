---
layout: practice
author: Alex Serban, Koen van der Blom, Joost Visser
name: Use Privacy-Preserving ML Techniques
category: Data
index: 7
unique_id: privacy_preserving
difficulty: na
references: [TTAID]
comments: True
description:
image: #
photocredit: #

intent: Provide privacy protection for individuals whose data is used in developing your ML application #
motivation: Many ML applications rely for training and operation on (sometimes large volumes of) data about people. As in any software application, this data should be handled with care, as stipulated by privacy regulations (e.g. GDPR), information security standards, and ethical criteria. Specifically for ML-applications, privacy risk may occur because of pooling data from different sources, sharing data sets for training, and deploying models trained with personal data. Privacy-preserving techniques can be applied to mitigate these risks. #
applicability: Consider using privacy-preserving ML techniques whenever you are using data about individuals, especially in case of personally identifiable information. #
related: [gov_responsible] #
dependencies: Similarities, differences and connections to other practices #
survey_question: 1 #
survey_item: We use privacy-preserving ML techniques (e.g. federated learning, differential privacy, or homomorphic encryption).

---

Whenever processing data that can be used to indentify or trace back information to individuals -- such as medical records -- it is compulsive to use privacy preserving techniques in order to protect the individuals' privacy.
Moreover, ML models are known to leak information (see membership attacks), and may reveal information about the training data

Anonymisation, pseudonymisation, differential privacy, federated ML or using cryptographic techniques -- such as homomorphic encryption -- are examples of privacy preserving ML techniques.

The tool support for privacy preserving ML is mature, with tools such as [Opacus](https://github.com/pytorch/opacus), [CrypTen](https://github.com/facebookresearch/CrypTen) or [PySift](https://github.com/OpenMined/PySyft) being developed and maintained by large research centres such as facebook AI research.