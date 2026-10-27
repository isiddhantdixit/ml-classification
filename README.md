
# Machine Learning Classification for Network Intrusion Detection

### A Comparative Analysis of Machine Learning Classification Algorithms Using Principal Component Analysis (PCA)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Machine%20Learning-Classification-orange?style=for-the-badge" alt="Machine Learning"/>
  <img src="https://img.shields.io/badge/Research-Network%20Security-red?style=for-the-badge" alt="Network Security"/>
  <img src="https://img.shields.io/badge/Dimensionality%20Reduction-PCA-blueviolet?style=for-the-badge" alt="PCA"/>
</p>

## 📌 Overview

This repository explores the application of machine learning classification algorithms to **network intrusion detection**, using the CIC-IDS2017 dataset.

The project investigates how **Principal Component Analysis (PCA)** can reduce the dimensionality of network traffic features while supporting the classification of benign and malicious network activity.

Multiple classification algorithms, PCA configurations, and train-test split ratios are compared to study their impact on model performance.

The project also forms the basis of our research paper, which follows the Springer research-paper format.

## 🎯 Objectives

- Analyze network traffic using the CIC-IDS2017 dataset.
- Apply PCA for dimensionality reduction.
- Compare different machine learning classification algorithms.
- Evaluate model performance across different PCA configurations.
- Investigate the effect of train-test split ratios on classification results.
- Explore machine learning techniques for cybersecurity and intrusion detection.

## 🧠 Machine Learning Algorithms

The study investigates the following algorithms:

| Algorithm | Purpose |
|---|---|
| Logistic Regression | Classification using a linear decision boundary |
| Linear Regression | Baseline comparison, with limitations for classification tasks |
| Linear Discriminant Analysis (LDA) | Classification through discriminant analysis |
| Quadratic Discriminant Analysis (QDA) | Classification using quadratic decision boundaries |
| Multi-Layer Perceptron (MLP) | Neural-network-based classification |

## 📊 Dataset

**Dataset:** CIC-IDS2017  
**Domain:** Network Security and Intrusion Detection

CIC-IDS2017 is a benchmark dataset containing benign network traffic and multiple types of simulated cyberattacks.

This project uses selected traffic records from the following captures:

- Tuesday – Working Hours
- Wednesday – Working Hours
- Thursday – Morning Web Attacks

Dataset source: [Canadian Institute for Cybersecurity – CIC-IDS2017](https://www.unb.ca/cic/datasets/ids-2017.html)

> Note: The experiments use selected portions of the original dataset rather than necessarily covering every capture and attack category.

## ⚙️ Methodology

The experimental workflow consists of the following stages:

1. **Data Preparation:** Load the selected CIC-IDS2017 traffic records.
2. **Preprocessing:** Prepare the data for machine learning and handle data-quality issues as implemented in the notebooks.
3. **Dimensionality Reduction:** Apply PCA using 5, 10, and 15 principal components.
4. **Model Training:** Train and evaluate the selected classification algorithms.
5. **Experimental Comparison:** Investigate three train-test split configurations.
6. **Performance Evaluation:** Compare the recorded model results to understand the influence of PCA and data partitioning.

### Experimental Design

| Parameter | Configurations |
|---|---|
| PCA components | 5, 10, 15 |
| Classification approaches | 5 |
| Train-test split ratios | 3 |
| Total experimental configurations | 45 |

The experimental design contains 45 possible model, PCA, and split combinations.

## 📈 Results

The recorded experimental results include a leading accuracy of **99.19%** for the MLP model using 15 PCA components with a 60:40 train-test split.

| Parameter | Best recorded configuration |
|---|---|
| Model | Multi-Layer Perceptron (MLP) |
| PCA components | 15 |
| Train-test split | 60:40 |
| Accuracy | 99.19% |

> **Important:** This is the best result recorded in the available experimental outputs, not a claim that every configuration has been independently verified. Performance should be interpreted alongside precision, recall, F1-score, class distribution, and the evaluation methodology.

## 🔬 Springer Research Paper

### A Comparative Analysis of Machine Learning Classification Algorithms Using Principal Component Analysis for Network Intrusion Detection

This research investigates the relationship between dimensionality reduction and classification performance in network intrusion detection.

The paper examines multiple machine learning approaches on selected CIC-IDS2017 data, evaluates different PCA component counts, and compares experimental train-test split configurations.

**Key research areas:**
- Comparative evaluation of machine learning classification algorithms.
- PCA-based dimensionality reduction for network traffic data.
- Performance comparison across different experimental configurations.
- Application of machine learning to cybersecurity and intrusion detection.

**Research contributions:**
- A structured experimental comparison of five classification approaches.
- An investigation of 5, 10, and 15 PCA components.
- Evaluation across three train-test split ratios.
- Analysis of the potential trade-offs between feature dimensionality and classification performance.

**Paper format:** Springer research-paper template  
**Research implementation:** Available in this repository.

> Publication status: Submitted

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Pandas** – Data manipulation and analysis
- **NumPy** – Numerical computation
- **Scikit-learn** – Machine learning algorithms and PCA
- **Matplotlib / Seaborn** – Data visualization, where used in the implementation
- **Jupyter Notebook** – Experimentation and analysis

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/isiddhantdixit/ml-classification.git
cd ml-classification
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install numpy pandas scikit-learn matplotlib seaborn jupyter
```

Install any additional dependencies required by the notebooks if applicable.

### 4. Prepare the dataset

Download CIC-IDS2017 from the [official dataset page](https://www.unb.ca/cic/datasets/ids-2017.html).

Place the required CSV files in the locations expected by the notebooks, or update the dataset paths in the code.

### 5. Run the experiments

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the relevant notebook in the repository and execute the cells in order. Follow the notebook's data preparation, PCA, training, and evaluation steps.

## 📁 Repository Structure

```text
ml-classification/
│
├── README.md
├── *.ipynb              # Experimental notebooks, if present
├── *.py                 # Python scripts, if present
├── *.csv                # Dataset or result files, if included
└── ...
```

The structure above is illustrative. Refer to the actual files in the repository for the current implementation and experiment outputs.

## 👥 Authors

- **Siddhant Dixit**
- **Ashutosh Kumar Jha**
- **Shashwat Bikram Singh**

## 🔮 Future Scope

- Evaluate additional classification algorithms and ensemble methods.
- Investigate alternative dimensionality-reduction techniques.
- Improve validation using stratified splits and cross-validation.
- Analyze class-wise precision, recall, and F1-scores.
- Investigate class imbalance and potential data leakage.
- Evaluate model generalization on unseen traffic and additional datasets.
- Explore deployment within a practical network intrusion detection pipeline.

## 📚 References

1. Sharafaldin, I., Lashkari, A. H., and Ghorbani, A. A. *Toward Generating a New Intrusion Detection Dataset and Intrusion Traffic Characterization.* Proceedings of the 4th International Conference on Information Systems Security and Privacy (ICISSP), 2018.
2. Canadian Institute for Cybersecurity. [CIC-IDS2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html).
3. Additional research references are documented in the accompanying research paper.



## 📄 License

This project currently does not include a dedicated `LICENSE` file.

The source code remains subject to applicable copyright laws. Public availability on GitHub does not automatically grant permission to reuse, modify, or redistribute the code.

A suitable open-source license, such as the **MIT License**, may be added in the future.

### Third-Party Materials

- **Dataset:** The CIC-IDS2017 dataset is subject to the terms and conditions specified by the Canadian Institute for Cybersecurity.
- **Research Paper:** The accompanying research paper and its contents may be subject to separate copyright and publication terms.
- **Dependencies:** Third-party libraries and tools retain their respective licenses.

For questions regarding reuse or distribution, please contact the repository owner.

