import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['Species'] = iris.target_names[iris.target]

# View basic statistical details for each species
species_details = iris_df.groupby('Species').describe().stack()
print("Basic Statistical Details for Each Species:")
print(species_details)

# Identify independent (features) and target variable
X = iris.data  # Using all features for simplicity
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a logistic regression model
model = LogisticRegression(random_state=42, max_iter=200)  # Increasing max_iter for convergence

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred, target_names=iris.target_names)

print("\nModel Evaluation:")
print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_rep)
