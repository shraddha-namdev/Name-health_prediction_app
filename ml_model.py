from sklearn.tree import DecisionTreeClassifier

# Training Data
X = [
    [180, 13, 200],
    [160, 12, 180],
    [100, 14, 180],
    [90, 10, 170],
    [110, 13, 260]
]

y = [
    "High Risk of Diabetes",
    "High Risk of Diabetes",
    "Normal Health Indicators",
    "Possible Anemia",
    "High Cholesterol Risk"
]

model = DecisionTreeClassifier()
model.fit(X, y)


def predict_health(glucose, haemoglobin, cholesterol):

    prediction = model.predict([
        [glucose, haemoglobin, cholesterol]
    ])

    return prediction[0]