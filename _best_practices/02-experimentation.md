---
layout: practice
author: András Schmelczer
name: Allow Experimentation with the Inference Function
title: Allow Experimentation with the Inference Function
category: Training
unique_id: training_experimentation
index: 26
difficulty: na
references: [GRADIO, STREAMLIT, GREATAI]
comments: True
description:
image:
photocredit:

intent: Gather feedback on the ML service before its production-ready deployment and allow efficiently iterating on it.
motivation: Involving more colleagues, specifically ones with different (non-technical) perspectives, early in the development can help catch issues quicker.
applicability: Allowing experimentation with the inference function early on should be a part of any mature ML lifecycle.
related: [interpretable, concerns]
dependencies: 
survey_question:

labels: [agility, effectiveness]

---

Next to proper documentation, models can also be evaluated qualitatively by interacting with them. Streamlining this process, especially for making it accessible to all stakeholders, can help in getting a shared understanding of the actual results and tightening the feedback loop.

These early deployments can be simply created with solutions such as <a href="https://gradio.app" target="_blank">Gradio</a> and <a href="https://streamlit.io/gallery" target="_blank">Streamlit</a>.

Additionally, the gathered insights should be easily fed back into the development. Thus, supporting rapid iterations should be part of implementing this best practice. A key component of good developer experience (DX) is _progressive evaluation_, through which development can become a highly iterative, experimental process. This is well-understood by popular data science tools, such as Jupyter Notebooks. Progressive evaluation can be implemented by making the inference functions code locally runnable and providing auto-reloading for their projects.
