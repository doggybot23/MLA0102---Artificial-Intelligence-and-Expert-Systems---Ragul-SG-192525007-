from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample dataset
X = [
    [25, 50000],
    [35, 65000],
    [45, 80000],
    [20, 20000],
    [50, 90000],
    [23, 25000],
    [40, 70000],
    [60, 100000]
]

# Loan Approved: 1 = Yes, 0 = No
y = [0, 1, 1, 0, 1, 0, 1, 1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Results
print("Predicted Loan Status:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
