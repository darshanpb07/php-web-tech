import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Load the dataset
fish_data = pd.read_csv('path/to/your/Fish.csv')

# Display the first few rows of the dataset
print(fish_data.head())

# Identify independent (features) and target variable
X = fish_data[['Length1', 'Length2', 'Length3', 'Height', 'Width']]
y = fish_data['Weight']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a simple linear regression model
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model Evaluation:")
print("Mean Squared Error (MSE):", mse)
print("R-squared (R2):", r2)

# Visualize the predictions vs actual values
plt.scatter(X_test['Length1'], y_test, color='black', label='Actual')
plt.scatter(X_test['Length1'], y_pred, color='blue', label='Predicted')
plt.xlabel('Length1')
plt.ylabel('Weight')
plt.legend()
plt.show()
