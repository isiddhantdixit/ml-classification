from pathlib import Path
import numpy as np
import pandas as pd

BASE_DIR = Path(r"C:\Users\siddh\Desktop\Python Project\MachineLearningCVE")

file1 = BASE_DIR / "Tuesday-WorkingHours.pcap_ISCX.csv"
file2 = BASE_DIR / "Wednesday-workingHours.pcap_ISCX.csv"
file3 = BASE_DIR / "Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv"

df1 = pd.read_csv(file1, low_memory=True)
df2 = pd.read_csv(file2, low_memory=True)
df3 = pd.read_csv(file3, low_memory=True)

dataset = pd.concat([df1, df2, df3], ignore_index=True)

dataset.columns = dataset.columns.str.strip()

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

X = X.apply(pd.to_numeric, errors='coerce')

X.replace([np.inf, -np.inf], np.nan, inplace=True)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X = imputer.fit_transform(X)

from sklearn.preprocessing import LabelEncoder

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.6,
    random_state=0,
    stratify=y
)

from sklearn.decomposition import PCA

pca = PCA(n_components=5)
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_pred = np.round(y_pred).astype(int)

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report

cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:\n")
print(cm)

print("\nAccuracy : {:.4f}".format(accuracy_score(y_test, y_pred)))
print("\nPrecision : {:.4f}".format(precision_score(y_test, y_pred, average='weighted', zero_division=0)))
print("\nRecall : {:.4f}".format(recall_score(y_test, y_pred, average='weighted', zero_division=0)))
print("\nF1 Score : {:.4f}".format(f1_score(y_test, y_pred, average='weighted', zero_division=0)))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))
