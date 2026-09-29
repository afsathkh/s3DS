import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

data = pd.read_csv('Iris.csv')

print(data.head())
print()

# Features
x = data.iloc[:, 1:5]

# Target
y = data.iloc[:, -1]

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42
)

# Create classifier
classifier = SVC(kernel='linear')
print(classifier)
print()

# Train the classifier
classifier.fit(x_train, y_train)

# Predict test data
y_pred = classifier.predict(x_test)

print("Predicted values:")
print(y_pred)
print()

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix")
print(cm)

# Accuracy
ac = accuracy_score(y_test, y_pred)
print("Accuracy Score", ac)
