# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example dataset: square footage vs house price
X = np.array([500, 800, 1000, 1200, 1500, 1800]).reshape(-1, 1)  # Feature
y = np.array([150000, 200000, 250000, 280000, 350000, 400000])   # Target

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make predictions
predicted = model.predict(X)

# Print slope and intercept
print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plot results
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, predicted, color="red", label="Regression Line")
plt.xlabel("Square Footage")
plt.ylabel("House Price")
plt.legend()
plt.show()