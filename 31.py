import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv('Iris.csv')

print("First few rows of the dataset:")
print(data.head())

# Features and target
x = data.iloc[:, :4]
y = data.iloc[:, -1]

print("\nFeatures (first 5 rows):")
print(x.head())

print("\nLabels (first 5 rows):")
print(y.head())

# Split dataset into training and testing data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.20, random_state=42
)

print("\nTraining features (first 5 rows):")
print(x_train.head())

print("\nTesting features (first 5 rows):")
print(x_test.head())

# Standardize the features
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Create Naive Bayes classifier
classifier = GaussianNB()

# Train the classifier
classifier.fit(x_train, y_train)

# Predict test data
y_pred = classifier.predict(x_test)

print("\nPredicted labels:")
print(y_pred)

print("\nActual labels:")
print(y_test.values)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Accuracy
ac = accuracy_score(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

print("\nAccuracy:")
print(ac)
