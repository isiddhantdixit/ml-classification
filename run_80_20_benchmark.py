"""
Automated 80:20 Benchmark Runner
Project: Comparative Analysis of ML Classification Algorithms with PCA (CIC-IDS2017)
Lead Contributor: Shashwat Bikram Singh (25BTRCN173)

Runs all 15 configurations of the 80:20 split suite and produces a consolidated
metrics summary table saved to CSV and Markdown.
"""

import os
import sys
from pathlib import Path
import numpy as np
import pandas as pd

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Import dataset loader
from dataset_loader import load_cicids_dataset

def run_suite():
    print("=" * 80)
    print("RUNNING 80:20 BENCHMARK SUITE - LEAD: SHASHWAT BIKRAM SINGH (25BTRCN173)")
    print("=" * 80)

    # 1. Load Data
    dataset = load_cicids_dataset()
    X = dataset.iloc[:, :-1].apply(pd.to_numeric, errors='coerce')
    X.replace([np.inf, -np.inf], np.nan, inplace=True)
    X = SimpleImputer(missing_values=np.nan, strategy='mean').fit_transform(X)

    labelencoder = LabelEncoder()
    y = labelencoder.fit_transform(dataset.iloc[:, -1])

    # 2. Train-test split (80:20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=0, stratify=y
    )

    models = [
        ("MLP", lambda: MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500, random_state=42), "classify"),
        ("LDA", lambda: LinearDiscriminantAnalysis(), "classify"),
        ("QDA", lambda: QuadraticDiscriminantAnalysis(reg_param=0.1), "classify"),
        ("Logistic Regression", lambda: LogisticRegression(max_iter=1000, random_state=0), "classify"),
        ("Rounded Linear Regression", lambda: LinearRegression(), "regress")
    ]

    components_list = [5, 10, 15]
    results = []

    for pca_dim in components_list:
        pca = PCA(n_components=pca_dim)
        X_tr = pca.fit_transform(X_train)
        X_te = pca.transform(X_test)

        for name, model_factory, m_type in models:
            print(f"Evaluating {name:26} | PCA: {pca_dim:2} ... ", end="", flush=True)
            model = model_factory()
            model.fit(X_tr, y_train)

            if m_type == "classify":
                preds = model.predict(X_te)
            else:
                preds = model.predict(X_te)
                preds = np.clip(np.round(preds).astype(int), 0, len(labelencoder.classes_) - 1)

            acc = accuracy_score(y_test, preds)
            prec = precision_score(y_test, preds, average='weighted', zero_division=0)
            rec = recall_score(y_test, preds, average='weighted', zero_division=0)
            f1 = f1_score(y_test, preds, average='weighted', zero_division=0)

            results.append({
                "Model": name,
                "Split": "80:20",
                "PCA": pca_dim,
                "Accuracy": f"{acc * 100:.2f}%",
                "Precision": f"{prec * 100:.2f}%",
                "Recall": f"{rec * 100:.2f}%",
                "Weighted F1": f"{f1 * 100:.2f}%",
                "Contributor": "Shashwat Bikram Singh"
            })
            print(f"Accuracy: {acc * 100:.2f}% | F1: {f1 * 100:.2f}%")

    df_results = pd.DataFrame(results)
    out_csv = Path(__file__).resolve().parent / "benchmark_results_80_20.csv"
    out_md = Path(__file__).resolve().parent / "benchmark_results_80_20.md"
    df_results.to_csv(out_csv, index=False)
    
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# 80:20 Benchmark Results (Lead: Shashwat Bikram Singh)\n\n")
        f.write(df_results.to_markdown(index=False))
        f.write("\n")

    print("\n" + "=" * 80)
    print("CONSOLIDATED 80:20 BENCHMARK RESULTS:")
    print("=" * 80)
    print(df_results.to_string(index=False))
    print(f"\nSaved results to:\n- {out_csv}\n- {out_md}\n")

if __name__ == "__main__":
    run_suite()

