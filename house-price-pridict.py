from sklearn.linear_model import LinearRegression
import numpy as np

# Input (size of house)
X = np.array([[1], [2], [3], [4], [5]])

# Output (price)
y = np.array([2, 4, 6, 8, 10])

# Model bana
model = LinearRegression()

# Train kar
model.fit(X, y)

# Predict kar
print(model.predict([[6]]))