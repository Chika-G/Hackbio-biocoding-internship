# Install required libraries
!pip install pandas numpy scikit-learn xgboost seaborn matplotlib

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import xgboost as xgb

# 🔹 Step 1: Load the dataset
url = "YOUR_GITHUB_RAW_LINK.csv"  # Replace with actual GitHub raw CSV link
df = pd.read_csv(url)

# Display dataset info
print("Dataset Info:")
print(df.info())

# Display first few rows
print("\nFirst 5 Rows:")
print(df.head())

# 🔹 Step 2: Preprocess the Data
# Select only numeric columns
df = df.select_dtypes(include=[np.number])

# Separate features (X) and target variable (y)
X = df.drop(columns=['score'])  # Features (chemical descriptors)
y = df['score']  # Target variable (docking score)

# Handle missing values by replacing with median
X.fillna(X.median(), inplace=True)

# Normalize the feature values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 🔹 Step 3: Split Data into Training and Testing Sets (80-20 split)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 🔹 Step 4: Train Regression Models

## 1️⃣ Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print("\n🔹 Linear Regression Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred_lr))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_lr)))
print("R² Score:", r2_score(y_test, y_pred_lr))

## 2️⃣ Random Forest Regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

print("\n🔹 Random Forest Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred_rf))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_rf)))
print("R² Score:", r2_score(y_test, y_pred_rf))

## 3️⃣ XGBoost Regressor
xgb_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=200, learning_rate=0.05)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

print("\n🔹 XGBoost Performance:")
print("MAE:", mean_absolute_error(y_test, y_pred_xgb))
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_xgb)))
print("R² Score:", r2_score(y_test, y_pred_xgb))

# 🔹 Step 5: Hyperparameter Optimization (for XGBoost)
param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 6, 9],
    'learning_rate': [0.01, 0.05, 0.1]
}

grid_search = GridSearchCV(xgb.XGBRegressor(objective='reg:squarederror'), param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_train, y_train)

print("\n🔹 Best Parameters for XGBoost:", grid_search.best_params_)

# 🔹 Step 6: Feature Importance Analysis
feature_importance = xgb_model.feature_importances_
sorted_idx = np.argsort(feature_importance)[::-1]

# Plot top 20 features
plt.figure(figsize=(10, 5))
sns.barplot(x=np.array(df.columns[:-1])[sorted_idx][:20], y=feature_importance[sorted_idx][:20])
plt.xticks(rotation=90)
plt.title("Top 20 Important Features for Docking Score Prediction")
plt.show()
