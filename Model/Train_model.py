# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the dataset with engineered features
df = pd.read_csv("weather_data_with_features.csv")

# Select features and target variable
features = [
    'humidity', 'wind_speed', 'pressure', 'precipitation', 'cloud_coverage',
    'month', 'day', 'hour', 'weekday', 'is_weekend',
    'season_encoded', 'wind_dir_encoded'
]
target = 'temperature'

# Define input (X) and output (y)
X = df[features]
y = df[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Model training complete")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)

# Save the trained model to a file
joblib.dump(model, "temperature_forecast_model.pkl")
print("Model saved as temperature_forecast_model.pkl")
