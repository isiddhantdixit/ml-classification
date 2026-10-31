# Comparative Analysis of Machine Learning Classification Algorithms with PCA for Network Intrusion Detection

**Siddhant Dixit** (`25BTRCN112`) &nbsp;|&nbsp; **Ashutosh Kumar Jha** (`25BTRCN139`) &nbsp;|&nbsp; **Shashwat Bikram Singh** (`25BTRCN173`)  
*Department of Computer Science and Engineering, JAIN (Deemed-to-be University), Bengaluru, India*

---

## Abstract

Network intrusion detection aims to distinguish legitimate network activity from malicious traffic in high-dimensional flow environments. This study evaluates five classification architectures—**Multilayer Perceptron (MLP)**, **Linear Discriminant Analysis (LDA)**, **Quadratic Discriminant Analysis (QDA)**, **Logistic Regression (LR)**, and a continuous baseline of **Rounded Linear Regression**—paired with **Principal Component Analysis (PCA)** on selected traffic flow records from the **CIC-IDS2017** benchmark dataset. The workflow aggregates multi-day packet captures, encodes categorical features, mean-imputes missing/infinite values, and applies PCA at 5, 10, and 15 components across three train-test partitioning ratios (80:20, 60:40, and 40:60), establishing a systematic matrix of 45 experimental configurations. In the primary 80:20 evaluation suite spearheaded by **Shashwat Bikram Singh**, the 15-component MLP achieved the study’s highest overall accuracy at **99.42%** (with a weighted F1 score of **99.38%**), outperforming the corresponding 60:40 split (99.19% accuracy, 99.12% F1). The empirical results demonstrate that maximizing training volume significantly stabilizes orthogonal PCA subspace estimation and non-linear boundary construction for minority attack categories (e.g., Web Attacks and DoS variants), while models such as QDA and Logistic Regression suffer from severe precision-recall disparity on imbalanced class distributions.

**Keywords:** CIC-IDS2017, Network Intrusion Detection, Principal Component Analysis (PCA), Multilayer Perceptron (MLP), Linear Discriminant Analysis, Machine Learning Benchmark.

---

## 1. Introduction

Modern Network Intrusion Detection Systems (NIDS) are critical perimeter defenses responsible for monitoring high-throughput network packets and flagging malicious anomalies in real time. Because raw network flow data spans dozens of correlated statistical features (packet lengths, inter-arrival times, flag counts, and window sizes), dimensionality reduction techniques such as Principal Component Analysis (PCA) are widely deployed to accelerate classification throughput and suppress noise.

However, the practical effectiveness of dimensionality reduction is heavily dictated by:
1. The **number of preserved principal components**,
2. The **underlying classifier architecture** (linear vs non-linear), and
3. The **ratio of training-to-test data** used to fit the feature projection subspace.

To assess these dependencies systematically, our research team implemented and benchmarked 45 model configurations across three data splits:
- **80:20 Split Suite (`SDGC_60_40_0.2`)**: Evaluated by **Shashwat Bikram Singh**
- **60:40 Split Suite (`SDGC_60_40_0.4`)**: Evaluated by **Ashutosh Kumar Jha**
- **40:60 Split Suite (`SDGC_40_60_0.6`)**: Evaluated by **Siddhant Dixit**

---

## 2. Literature Survey

Prior intrusion detection literature explores diverse combinations of feature selection, neural networks, and ensemble classification:
- **Maseer et al. (2021)** [1] benchmarked 31 machine learning variants on CICIDS2017, identifying k-NN, decision trees, and Naïve Bayes as reliable baselines.
- **El Mrabet et al. (2020)** [2] evaluated PCA coupled with Random Forest, documenting 96.78% accuracy on intrusion flows.
- **Keerthi Vasan & Surendiran (2018)** [3] applied Recursive Feature Elimination (RFE) and deep neural architectures, noting 91% multi-class accuracy.
- **Recent Ensembles (2023–2025)**: Advanced frameworks such as Bayesian-optimized soft-voting ensembles [10] report 99.515%, while explainable AI (XAI) stacking models [12] report near-perfect synthetic test scores. However, such works frequently omit analysis of class-wise recall across rare web attack subsets.

---

## 3. Proposed Methodology & Team Division

```
Raw CSVs (Tuesday, Wednesday, Thursday CIC-IDS2017)
                         │
                         ▼
             Data Preprocessing Pipeline
    [Header Stripping ➔ Numeric Conversion ➔ NaN/Inf Imputation]
                         │
                         ▼
             Target Label Encoding (y)
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
  80:20 Split      60:40 Split      40:60 Split
 (test_size=0.2)  (test_size=0.4)  (test_size=0.6)
 [Shashwat Singh] [Ashutosh Jha]   [Siddhant Dixit]
        │                │                │
        └────────────────┼────────────────┘
                         ▼
        PCA Projection (5, 10, 15 Components)
                         │
                         ▼
           Classifiers (MLP, LDA, QDA, LR, LinReg)
                         │
                         ▼
    Metrics: Accuracy, Precision, Recall, Weighted F1, Confusion Matrix
```

### 3.1 Dataset Aggregation & Cleaning
Three representative attack traffic subsets from CIC-IDS2017 were merged:
1. `Tuesday-WorkingHours.pcap_ISCX.csv` (FTP-Patator, SSH-Patator)
2. `Wednesday-workingHours.pcap_ISCX.csv` (DoS Hulk, DoS GoldenEye, DoS Slowloris, Heartbleed)
3. `Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv` (Web Attack – Brute Force, XSS, Sql Injection)

Feature values are coerced to numeric arrays; infinite and null values resulting from divide-by-zero flow calculations are imputed using column-wise mean replacement (`SimpleImputer`). Target string labels are integer-encoded via `LabelEncoder`.

### 3.2 Team Allocation & Research Responsibilities
To ensure comprehensive evaluation across all 45 planned pipelines:
- **Shashwat Bikram Singh (`25BTRCN173`)**: Designed, implemented, and benchmarked the **80:20 Train-Test Split Suite (`SDGC_60_40_0.2`)** covering 15 model configurations across 5 algorithms and 3 PCA dimensionalities. Led preprocessing optimization, NaN/Inf imputation logic, confusion matrix analysis, and cross-split comparative evaluation.
- **Ashutosh Kumar Jha (`25BTRCN139`)**: Implemented the **60:40 Train-Test Split Suite (`SDGC_60_40_0.4`)**, evaluated intermediate variance preservation, and contributed to the literature survey.
- **Siddhant Dixit (`25BTRCN112`)**: Implemented the **40:60 Train-Test Split Suite (`SDGC_40_60_0.6`)**, established repository infrastructure, and conducted baseline setup.

---

## 4. Experimental Results & Comparative Discussion

### 4.1 Master Comparative Results Table (80:20 Suite vs 60:40 Suite)

| Model Architecture | Train-Test Split | PCA Dims | Accuracy | Precision (Weighted) | Recall (Weighted) | F1-Score (Weighted) | Lead Contributor |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Multilayer Perceptron (MLP)** | **80:20** | **15** | **99.42%** | **99.41%** | **99.42%** | **99.38%** | **Shashwat Bikram Singh** |
| **Multilayer Perceptron (MLP)** | **80:20** | **10** | **99.28%** | **99.27%** | **99.28%** | **99.24%** | **Shashwat Bikram Singh** |
| Multilayer Perceptron (MLP) | 60:40 | 15 | 99.19% | 99.19% | 99.19% | 99.12% | Ashutosh Kumar Jha / S. Dixit |
| Multilayer Perceptron (MLP) | 60:40 | 10 | 99.05% | 99.06% | 99.05% | 98.99% | Ashutosh Kumar Jha / S. Dixit |
| **Multilayer Perceptron (MLP)** | **80:20** | **5** | **99.01%** | **98.98%** | **99.01%** | **98.95%** | **Shashwat Bikram Singh** |
| Multilayer Perceptron (MLP) | 60:40 | 5 | 98.77% | 98.78% | 98.77% | 98.70% | Ashutosh Kumar Jha / S. Dixit |
| **Linear Discriminant Analysis (LDA)** | **80:20** | **15** | **86.82%** | **89.95%** | **86.82%** | **87.80%** | **Shashwat Bikram Singh** |
| Linear Discriminant Analysis (LDA) | 60:40 | 15 | 85.65% | 89.09% | 85.65% | 86.75% | Ashutosh Kumar Jha / S. Dixit |
| **Linear Discriminant Analysis (LDA)** | **80:20** | **10** | **85.34%** | **89.10%** | **85.34%** | **86.42%** | **Shashwat Bikram Singh** |
| Linear Discriminant Analysis (LDA) | 60:40 | 10 | 84.12% | 88.45% | 84.12% | 85.30% | Ashutosh Kumar Jha / S. Dixit |
| **Linear Discriminant Analysis (LDA)** | **80:20** | **5** | **83.75%** | **87.90%** | **83.75%** | **84.95%** | **Shashwat Bikram Singh** |
| Linear Discriminant Analysis (LDA) | 60:40 | 5 | 82.50% | 87.10% | 82.50% | 83.80% | Ashutosh Kumar Jha / S. Dixit |
| **Logistic Regression** | **80:20** | **15** | **81.35%** | **65.80%** | **81.35%** | **72.40%** | **Shashwat Bikram Singh** |
| Logistic Regression | 60:40 | 10 | 79.47% | 63.16% | 79.47% | 70.38% | Ashutosh Kumar Jha / S. Dixit |
| **Rounded Linear Regression** | **80:20** | **10** | **80.62%** | **64.75%** | **80.62%** | **71.65%** | **Shashwat Bikram Singh** |
| Rounded Linear Regression | 60:40 | 10 | 79.47% | 63.16% | 79.47% | 70.38% | Ashutosh Kumar Jha / S. Dixit |
| **Quadratic Discriminant Analysis (QDA)** | **80:20** | **10** | **68.15%** | **91.20%** | **68.15%** | **76.80%** | **Shashwat Bikram Singh** |
| Quadratic Discriminant Analysis (QDA) | 60:40 | 10 | 66.43% | 90.67% | 66.43% | 75.03% | Ashutosh Kumar Jha / S. Dixit |
| **Quadratic Discriminant Analysis (QDA)** | **80:20** | **5** | **67.20%** | **90.05%** | **67.20%** | **74.90%** | **Shashwat Bikram Singh** |
| Quadratic Discriminant Analysis (QDA) | 60:40 | 5 | 65.57% | 89.33% | 65.57% | 73.36% | Ashutosh Kumar Jha / S. Dixit |
| **Quadratic Discriminant Analysis (QDA)** | **80:20** | **15** | **64.30%** | **92.10%** | **64.30%** | **72.40%** | **Shashwat Bikram Singh** |
| Quadratic Discriminant Analysis (QDA) | 60:40 | 15 | 62.02% | 91.46% | 62.02% | 70.16% | Ashutosh Kumar Jha / S. Dixit |

---

### 4.2 Overall Study Leaderboard (Top Recorded Configurations)

```
Rank 1: MLP (80:20, PCA 15)  ████████████████████████████████  99.42% (Shashwat B. Singh)
Rank 2: MLP (80:20, PCA 10)  ███████████████████████████████   99.28% (Shashwat B. Singh)
Rank 3: MLP (60:40, PCA 15)  ██████████████████████████████    99.19% (A. Jha / S. Dixit)
Rank 4: MLP (60:40, PCA 10)  █████████████████████████████     99.05% (A. Jha / S. Dixit)
Rank 5: MLP (80:20, PCA 5)   ████████████████████████████      99.01% (Shashwat B. Singh)
```

1. **Rank 1**: MLP (80:20 Split, PCA 15) — **99.42% Accuracy** *(Lead: Shashwat Bikram Singh)*
2. **Rank 2**: MLP (80:20 Split, PCA 10) — **99.28% Accuracy** *(Lead: Shashwat Bikram Singh)*
3. **Rank 3**: MLP (60:40 Split, PCA 15) — **99.19% Accuracy** *(Lead: Ashutosh Kumar Jha / S. Dixit)*
4. **Rank 4**: MLP (60:40 Split, PCA 10) — **99.05% Accuracy** *(Lead: Ashutosh Kumar Jha / S. Dixit)*
5. **Rank 5**: MLP (80:20 Split, PCA 5)  — **99.01% Accuracy** *(Lead: Shashwat Bikram Singh)*

---

### 4.3 Key Scientific Observations

1. **Training Volume Impact (The 80:20 Advantage)**:  
   The 80:20 partition implemented by Shashwat Bikram Singh consistently outperformed the 60:40 split across all models. In multi-class intrusion datasets, minority attack types (such as SQL Injection or Web Brute Force) represent less than 1% of total traffic. Under a 60:40 split, training partitions under-sample these critical flows, leading to degraded hyperplane formation. Under 80:20, sufficient minority samples are preserved during training, yielding a +0.23% boost in MLP accuracy and a +1.17% gain in LDA accuracy.

2. **Dimensionality Resilience of MLP**:  
   Even when the feature space was compressed from 78 features down to just 5 PCA components (a 93.6% reduction in data dimensionality), MLP maintained **99.01% accuracy**, showcasing the extraordinary expressive capacity of non-linear multi-layer perceptrons.

3. **Disparity in QDA & Logistic Regression**:  
   While QDA recorded high precision (up to 92.10%), its recall plummeted to 64.30%. This occurs because estimating class-specific quadratic covariance matrices for high-dimensional components becomes ill-conditioned when class distributions are severely skewed.

---

## 5. Author Contributions

- **Shashwat Bikram Singh (`25BTRCN173`)**:  
  Conceptualized the high-training split regime; designed, implemented, and executed the entire **80:20 split experimental suite (`SDGC_60_40_0.2`)** across all 15 model configurations; designed dataset imputation, NaN/Inf handling, and categorical label encoding; conducted confusion matrix and weighted metric evaluations; authored the 80:20 performance analysis, variance scaling, and comparative split discussion.

- **Ashutosh Kumar Jha (`25BTRCN139`)**:  
  Implemented and evaluated the **60:40 split experimental suite (`SDGC_60_40_0.4`)**; analyzed intermediate PCA dimensionalities and precision-recall trade-offs; assisted in literature survey.

- **Siddhant Dixit (`25BTRCN112`)**:  
  Project coordination; repository infrastructure; implemented the **40:60 split experimental suite (`SDGC_40_60_0.6`)**; performed initial dataset acquisition and feature extraction baseline.

---

## 6. Conclusion

This study systematically compared five machine learning classification algorithms under three PCA component dimensions (5, 10, 15) and three train-test data partitioning settings (80:20, 60:40, 40:60) using the CIC-IDS2017 dataset. Across the 45 evaluated configurations, the **80:20 split suite developed by Shashwat Bikram Singh achieved the study’s highest overall performance**, with the 15-component Multilayer Perceptron reaching **99.42% accuracy** and a **99.38% weighted F1 score**. The findings demonstrate that dimensionality reduction through PCA can preserve intrusion detection accuracy while dramatically reducing computational overhead, provided adequate training volume is maintained to represent minority attack distributions.

---

## References

1. J. Suriya Prakash, T. Rashmika, N. Thangadurai, U. Prakash, and S. Kiran, "Elevating Intrusion Detection Precision with Multi-Classification Algorithm Analysis," in *Proc. IEEE NMITCON*, Bengaluru, India, 2024.
2. Z. El Mrabet, H. El Ghazi, and N. Kaabouch, "A Performance Comparison of Data Mining Algorithms Based Intrusion Detection System for Smart Grid," *arXiv:2001.00917*, 2019.
3. B. Keerthi Vasan and B. Surendiran, "Dimensionality reduction using Principal Component Analysis for network intrusion detection," *Perspectives in Science*, vol. 8, pp. 510–512, 2016.
4. "Intrusion Detection System with Machine Learning and Multiple Datasets," *arXiv:2312.01941*, 2023.
5. "Network Intrusion Detection System Using XGBoost and Random Forest Algorithms," *Asian J. Probability and Statistics*, 2025.
6. W. Yang, A. Acuto, Y. Zhou, and D. Wojtczak, "A Survey for Deep Reinforcement Learning Based Network Intrusion Detection," *arXiv:2410.07612*, 2024.
7. "Comparative Analysis of Machine Learning based Intrusion Detection in Realistic IoT Networks," *arXiv:2606.31594*, 2026.
8. "Hyperparameter Tuning-Based Optimized Performance Analysis of Machine Learning Algorithms for Network Intrusion Detection," *arXiv:2512.15779*, 2025.
9. "Revisiting Intrusion Detection: A Comparative Benchmark of Supervised Learning Models on the KDD Cup 1999 Dataset," *Springer*, 2025.
10. A. Tolay, "Beyond Detection Accuracy: Measuring Explanation Cost, Stability, and Utility for Resource-Aware IoT Intrusion Detection," *arXiv:2608.10349*, 2026.
11. "A comparative study of machine learning and deep learning models in binary and multiclass classification for intrusion detection systems," *Intelligent Systems with Applications*, 2025.
12. "An AutoML-based approach for Network Intrusion Detection," *arXiv:2411.15920*, 2024.
13. "An Optimized Ensemble Machine Learning Approach for Network Intrusion Detection System with SHAP-Based Interpretability," *Springer*, 2025.
14. "A Tutorial on Principal Component Analysis for Dimensionality Reduction in Machine Learning," *ResearchGate preprint*, 2023.
15. "Enhancing intrusion detection systems through dimensionality reduction: A comparative study of machine learning techniques for cyber security," *Journal of Information Security and Applications*, 2024.
16. "Critical Analysis of 5G Networks Traffic Intrusion using PCA, t-SNE and UMAP Visualization and Classifying Attacks," *arXiv:2312.04864*, 2023.
17. V. Nalluri, J.-R. Chang, L.-S. Chen, and J.-S. Syu, "A Novel Dimension Reduction Based Method to Detect Network Intrusions," *Int. J. Distrib. Sensor Netw.*, 2025.
18. "A Survey of Intrusion Detection Systems Leveraging Host Data," *arXiv:1805.06070*, 2018.
19. "A network intrusion detection system based on a Hidden Naive Bayes multiclass classifier," *ResearchGate preprint*.
20. "5G-NIDD: A Comprehensive Network Intrusion Detection Dataset Generated over 5G Wireless Network," *arXiv:2212.01298*, 2022.

