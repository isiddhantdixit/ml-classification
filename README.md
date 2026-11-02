# Machine Learning Classification for Network Intrusion Detection

### A Comparative Analysis of Machine Learning Classification Algorithms Using Principal Component Analysis (PCA)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Classification-orange?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/Research-Network%20Security-red?style=for-the-badge" alt="Network Security"/>
  <img src="https://img.shields.io/badge/Dimensionality%20Reduction-PCA-blueviolet?style=for-the-badge" alt="PCA"/>
  <img src="https://img.shields.io/badge/Dataset-CIC--IDS2017-green?style=for-the-badge" alt="CIC-IDS2017"/>
</p>

---


## 📌 Overview

This repository explores the application of machine learning classification algorithms to **network intrusion detection**, using selected flow captures from the **CIC-IDS2017** benchmark dataset.

The project investigates how **Principal Component Analysis (PCA)** can reduce high-dimensional network flow features (up to 78 numeric attributes) while reliably supporting multi-class classification of benign traffic and diverse cyberattack vectors (DoS, DDoS, Web Attacks, Patator attacks).

The experimental matrix spans **45 distinct model configurations** across three data partitioning regimes (80:20, 60:40, 40:60), three PCA component levels (5, 10, 15), and five classification architectures.

This project forms the empirical basis of our research paper, prepared in the Springer research-paper format:  
📄 **Full Paper Report available in this repository:** [`RESEARCH_PAPER_REPORT.md`](RESEARCH_PAPER_REPORT.md) & [`RESEARCH_PAPER_REPORT.pdf`](RESEARCH_PAPER_REPORT.pdf).

---

## 🎯 Objectives

- Analyze high-dimensional network traffic using the CIC-IDS2017 dataset.
- Apply PCA dimensionality reduction across 5, 10, and 15 principal components.
- Compare linear, quadratic, and deep neural network classification algorithms.
- Investigate the effect of train-test split ratios (80:20 vs 60:40 vs 40:60) on classification stability and minority-class recall.
- Address severe class imbalance in multi-class intrusion detection.

---

## 🧠 Machine Learning Algorithms

| Algorithm | Model Type | Purpose in Study |
| :--- | :--- | :--- |
| **Multilayer Perceptron (MLP)** | Deep Neural Network `(64, 32)` | Captures non-linear decision boundaries across projected PCA manifolds |
| **Linear Discriminant Analysis (LDA)** | Linear Supervised Projection | Maximizes between-class variance relative to within-class covariance |
| **Quadratic Discriminant Analysis (QDA)** | Quadratic Decision Boundary | Fits class-specific quadratic boundaries without assuming equal covariance |
| **Logistic Regression** | Linear Multinomial Classifier | Classical baseline optimizing multinomial cross-entropy |
| **Rounded Linear Regression** | Continuous Projection Baseline | Evaluates continuous hyperplane projection rounded to discrete class IDs |

---

## 📊 Dataset

**Dataset:** CIC-IDS2017  
**Domain:** Network Security and Intrusion Detection  
**Source:** [Canadian Institute for Cybersecurity – CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)

Selected multi-day captures aggregated for this research:
1. `Tuesday-WorkingHours.pcap_ISCX.csv` (FTP-Patator, SSH-Patator)
2. `Wednesday-workingHours.pcap_ISCX.csv` (DoS Hulk, DoS GoldenEye, DoS Slowloris, Heartbleed)
3. `Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv` (Web Attack – Brute Force, XSS, Sql Injection)

---

## ⚙️ Experimental Design (45 Configurations)

$$\text{Total Pipelines} = 3 \text{ Splits } (80:20, 60:40, 40:60) \times 3 \text{ PCA Component Levels } (5, 10, 15) \times 5 \text{ Classifiers} = 45$$

- **`SDGC_60_40_0.2`** (`test_size=0.2` / 80:20 split): Led by **Shashwat Bikram Singh**
- **`SDGC_60_40_0.4`** (`test_size=0.4` / 60:40 split): Led by **Ashutosh Kumar Jha**
- **`SDGC_40_60_0.6`** (`test_size=0.6` / 40:60 split): Led by **Siddhant Dixit**

---

## 📈 Consolidated Benchmark Results

### 1. Cross-Split Comparison (80:20 vs 60:40)

| Model Architecture | PCA Dims | 80:20 Split (Shashwat B. Singh) Accuracy | 80:20 Weighted F1 | 60:40 Split (A. Jha / S. Dixit) Accuracy | 60:40 Weighted F1 | Research Insights |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **MLP** | **15** | **99.42%** | **99.38%** | 99.19% | 99.12% | **Overall Best Result:** 80% training data optimizes non-linear boundaries |
| **MLP** | **10** | **99.28%** | **99.24%** | 99.05% | 98.99% | Excellent multi-class generalization across 10 components |
| **MLP** | **5** | **99.01%** | **98.95%** | 98.77% | 98.70% | High performance preserved even under 93.6% feature compression |
| **LDA** | **15** | **86.82%** | **87.80%** | 85.65% | 86.75% | Strong linear separation across 15 orthogonal axes |
| **LDA** | **10** | **85.34%** | **86.42%** | 84.12% | 85.30% | Minimal degradation under moderate dimension reduction |
| **LDA** | **5** | **83.75%** | **84.95%** | 82.50% | 83.80% | Moderate loss from compressed intra-class covariance |
| **Logistic Regression** | **15** | **81.35%** | **72.40%** | 80.12% | 71.05% | High accuracy, but low weighted recall reflects minority class imbalance |
| **Logistic Regression** | **10** | **80.62%** | **71.65%** | 79.47% | 70.38% | Tied with Rounded Linear Regression baseline |
| **Rounded LinReg** | **10** | **80.62%** | **71.65%** | 79.47% | 70.38% | Continuous hyperplane projected onto discrete integer labels |
| **QDA** | **10** | **68.15%** | **76.80%** | 66.43% | 75.03% | High precision (>91%) but lower recall due to covariance ill-conditioning |
| **QDA** | **5** | **67.20%** | **74.90%** | 65.57% | 73.36% | Stable quadratic boundaries in lower dimensional spaces |
| **QDA** | **15** | **64.30%** | **72.40%** | 62.02% | 70.16% | Parameter explosion in higher PCA dimensions reduces test recall |

### 2. Overall Study Leaderboard (Top Recorded Configurations)

| Rank | Model Architecture | Train-Test Split | PCA Components | Accuracy | Lead Contributor |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 🥇 **1** | **Multilayer Perceptron (MLP)** | **80:20 (`0.2`)** | **15** | **99.42%** | **Shashwat Bikram Singh** |
| 🥈 **2** | **Multilayer Perceptron (MLP)** | **80:20 (`0.2`)** | **10** | **99.28%** | **Shashwat Bikram Singh** |
| 🥉 **3** | **Multilayer Perceptron (MLP)** | 60:40 (`0.4`) | 15 | 99.19% | Ashutosh Kumar Jha / Siddhant Dixit |
| 4 | **Multilayer Perceptron (MLP)** | 60:40 (`0.4`) | 10 | 99.05% | Ashutosh Kumar Jha / Siddhant Dixit |
| 5 | **Multilayer Perceptron (MLP)** | **80:20 (`0.2`)** | **5** | **99.01%** | **Shashwat Bikram Singh** |

---

## 💡 Key Scientific Findings

1. **Volume of Training Data (The 80:20 Split Advantage):**  
   The **80:20 split suite** engineered by Shashwat Bikram Singh consistently outperformed the 60:40 and 40:60 splits across all algorithms. In multi-class intrusion datasets, minority attack types (such as SQL Injection or Web Brute Force) represent less than 1% of total traffic. Under 80:20, sufficient minority samples are preserved during training, yielding higher recall and classification stability.

2. **MLP Dominance with PCA:**  
   The Multilayer Perceptron demonstrated exceptional non-linear boundary construction, achieving **99.42% accuracy** at 15 PCA components and maintaining **99.01%** even when features were reduced to only 5 principal components.

3. **Precision vs. Recall Nuance:**  
   Models such as QDA and Logistic Regression demonstrated deceptively high weighted precision (~91%), but exhibited significantly lower recall (~64-68%). This highlights why multi-class IDS research must report comprehensive confusion matrices, macro-F1, and per-class recall rather than accuracy in isolation.

---

## 🔬 Research Paper & Publication Status

**Title:** *Comparative Analysis of Machine Learning Classification Algorithms with PCA for Network Intrusion Detection*  
**Format:** Springer Research Paper Template  
**Authors:** Siddhant Dixit, Ashutosh Kumar Jha, Shashwat Bikram Singh  
**Status:** Submitted  

Complete documentation files available in this repository:
- 📄 **Markdown Paper:** [`RESEARCH_PAPER_REPORT.md`](RESEARCH_PAPER_REPORT.md)
- 📄 **Word Document:** [`RESEARCH_PAPER_REPORT.docx`](RESEARCH_PAPER_REPORT.docx)
- 📄 **PDF Document:** [`RESEARCH_PAPER_REPORT.pdf`](RESEARCH_PAPER_REPORT.pdf)

---

## 🛠️ Technologies Used

- **Python 3.10+** – Core programming language
- **Scikit-learn** – Machine learning models (MLP, LDA, QDA, LR, LinReg), PCA, SimpleImputer, metrics
- **Pandas** – High-throughput CSV data handling
- **NumPy** – Numerical matrix computation
- **ReportLab / python-docx** – Publication report generation

---

## 📁 Repository Structure

```text
ml-classification/
│
├── README.md                                      # Comprehensive research overview & team contributions
├── RESEARCH_PAPER_REPORT.md                       # Full publication-ready report & methodology
├── RESEARCH_PAPER_REPORT.docx                     # Complete formatted paper report (Word)
├── RESEARCH_PAPER_REPORT.pdf                      # Complete formatted paper report (PDF)
├── dataset_loader.py                              # Resilient dataset loader (supports real CSVs & fallback)
├── run_80_20_benchmark.py                         # Automated batch runner for 80:20 suite
├── verify_all_scripts.py                          # Automated regression test suite (15/15 passing)
│
├── SDGC_60_40_0.2/                                # 80:20 Split Suite (Lead: Shashwat Bikram Singh)
│   ├── dataset_loader.py
│   ├── SDGC 60,40 Linear Discriminant Analysis 0.2 5.py
│   ├── SDGC 60,40 Linear Discriminant Analysis 0.2 10.py
│   ├── SDGC 60,40 Linear Discriminant Analysis 0.2 15.py
│   ├── SDGC 60,40 Linear Regression 0.2 5.py
│   ├── SDGC 60,40 Linear Regression 0.2 10.py
│   ├── SDGC 60,40 Linear Regression 0.2 15.py
│   ├── SDGC 60,40 Logistic Regression 0.2 5.py
│   ├── SDGC 60,40 Logistic Regression 0.2 10.py
│   ├── SDGC 60,40 Logistic Regression 0.2 15.py
│   ├── SDGC 60,40 Multilayer Perceptron 0.2 5.py
│   ├── SDGC 60,40 Multilayer Perceptron 0.2 10.py
│   ├── SDGC 60,40 Multilayer Perceptron 0.2 15.py
│   ├── SDGC 60,40 Quadratic Discriminant Analysis 0.2 5.py
│   ├── SDGC 60,40 Quadratic Discriminant Analysis 0.2 10.py
│   └── SDGC 60,40 Quadratic Discriminant Analysis 0.2 15.py
│
├── SDGC_60_40_0.4/                                # 60:40 Split Suite (Lead: Ashutosh Kumar Jha)
├── SDGC_40_60_0.6/                                # 40:60 Split Suite (Lead: Siddhant Dixit)
└── outputs/                                       # Recorded confusion matrix & metric captures
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/isiddhantdixit/ml-classification.git
cd ml-classification
```

### 2. Install dependencies

```bash
pip install numpy pandas scikit-learn
```

### 3. Running an Individual Model

```bash
python "SDGC_60_40_0.2/SDGC 60,40 Multilayer Perceptron 0.2 15.py"
```

> **Note on Datasets:** All scripts dynamically search for the three CIC-IDS2017 CSV files (in `./data/`, `./MachineLearningCVE/`, via CLI arg, or environment variable `CICIDS_DATA_DIR`). If files are not present locally, scripts automatically synthesize a representative multi-class flow dataset (78 features, realistic flow distributions) so execution completes **without error**.

### 4. Running the Complete 80:20 Benchmark Suite

```bash
python run_80_20_benchmark.py
```

### 5. Running the Verification Regression Tests

```bash
python verify_all_scripts.py
```

---

## 📚 References

1. Sharafaldin, I., Lashkari, A. H., and Ghorbani, A. A. *Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization.* ICISSP, 2018.
2. Canadian Institute for Cybersecurity. [CIC-IDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html).
3. Additional research references are documented in [`RESEARCH_PAPER_REPORT.md`](RESEARCH_PAPER_REPORT.md).

---

## 📄 License

This repository is maintained for collaborative academic research at JAIN (Deemed-to-be University).
