# 🧠 Predicting ADHD in Women Using Brain Connectome Matrices

This project explores the use of machine learning to predict **Attention-Deficit/Hyperactivity Disorder (ADHD)** in women using brain connectome data, psychosocial indicators, and demographic features. The model leverages neuroimaging-derived connectivity matrices alongside behavioral assessments like the SDQ (Strengths and Difficulties Questionnaire) to improve early detection, particularly for females, where ADHD remains historically underdiagnosed.

---

## 🌟 Motivation

ADHD in females is often missed or misdiagnosed due to less overt hyperactive behavior and diagnostic criteria primarily derived from male populations. Undiagnosed ADHD can lead to lifelong issues with academic achievement, career progression, and mental health.

This project aims to:
- Build an early-warning system using neurobiological and behavioral features,
- Close the gender gap in diagnosis,
- Inform targeted interventions through interpretable machine learning.

---

## ⚡ Why DuckDB for Data Merging?

Given the size and structure of the dataset—multiple sources including:
- Brain connectome matrices,
- SDQ scores,
- Demographics and labels—

we chose **DuckDB**, a high-performance in-memory SQL engine, to simplify and accelerate data manipulation. DuckDB allowed us to:

- Perform **SQL-style joins and aggregations** directly on Parquet or CSV files,
- Avoid memory bottlenecks with large datasets,
- Improve development **speed and interactivity** within Jupyter notebooks,
- Ensure **scalability** for potential future expansions (e.g., adding more imaging features or multi-center data).

---

## 🧠 Challenge: High-Dimensional Brain Connectome Data

Brain connectome matrices represent functional or structural connectivity between dozens of brain regions, resulting in **hundreds to thousands of features** when flattened (e.g., upper triangle of a correlation matrix). This introduces several issues:

- 🚨 **Curse of dimensionality**: Too many features relative to the number of subjects can cause overfitting.
- 🧮 **Computational inefficiency**: Training becomes slower and noisier.
- 🔍 **Redundancy**: Many connectome features may be highly correlated or irrelevant to the prediction task.

To address this, we used **Principal Component Analysis (PCA)** to:

- Reduce dimensionality while retaining most of the variance,
- Compress noisy, sparse, or redundant data into a smaller set of informative components,
- Improve model generalization and interpretability.

---

## 🧪 Importance of SDQ in ADHD Prediction

The **Strengths and Difficulties Questionnaire (SDQ)** is a validated behavioral assessment tool that screens for mental health issues in youth. It captures ADHD-relevant traits such as:

- Hyperactivity,
- Emotional regulation,
- Peer issues,
- Conduct behavior.

Including SDQ scores in the model added behavioral context to the brain-based features, improving sensitivity to real-world diagnostic patterns and reducing reliance on neuroimaging alone.

---

## 🎯 Methodology Highlights

- 🧩 Multimodal feature integration: connectome + SDQ + demographics.
- 🧠 PCA to reduce high-dimensional brain features.
- 🧪 MLP and other classifiers for multi-label ADHD prediction.
- ⚖️ F1-score-based evaluation, with attention to class imbalance (especially for female ADHD).

---

## 🌍 UN SDG Alignment

This research aligns with key Sustainable Development Goals:

- **SDG 3 – Good Health and Well-being**: Early identification enables timely treatment and better mental health outcomes.
- **SDG 4 – Quality Education**: Supports at-risk students in achieving academic success.
- **SDG 5 – Gender Equality**: Addresses underdiagnosis of ADHD in women and girls.

---

## 📁 Project Structure

- `mlp.ipynb`: Neural network model training and evaluation.
- `analysis_notebook.ipynb`: Data exploration and connectome-SDQ correlation analysis.



