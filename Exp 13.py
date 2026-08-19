from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Patient data: [Age, Temperature, Cough]
X = [
    [25, 98, 0],
    [35, 101, 1],
    [45, 102, 1],
    [20, 97, 0],
    [50, 103, 1],
    [30, 99, 0],
    [60, 104, 1],
    [40, 100, 1]
]

# 0 = No Disease, 1 = Disease
y = [0, 1, 1, 0, 1, 0, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000, random_state=42)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
