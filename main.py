import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
file_path = "partial_credit.csv"
df = pd.read_csv(file_path)

# Drop the irrelevant column
df = df.drop(columns=["Unnamed: 0"], errors='ignore')

# Define features and target variable
X = df.drop(columns=["Class"])  # Features
y = df["Class"]  # Target

# Standardize the feature set for better SVM performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into 70% training and 30% testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42, stratify=y)

# Define and train SVM models with different kernels
kernels = ["linear", "poly", "rbf"]
models = {kernel: SVC(kernel=kernel, random_state=42) for kernel in kernels}

for kernel, model in models.items():
    model.fit(X_train, y_train)

# Evaluate models
results = {}
for kernel, model in models.items():
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    results[kernel] = {"accuracy": accuracy, "report": report}

# Print results
for kernel, result in results.items():
    print(f"SVM with {kernel} kernel:")
    print(f"Accuracy: {result['accuracy']:.4f}")
    print("Classification Report:")
    print(result['report'])
    print("-" * 50)
