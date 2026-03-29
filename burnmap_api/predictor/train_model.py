import json
import pickle
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load mock dataset
with open("mock_dataset.json", "r") as f:
    dataset = json.load(f)

df = pd.DataFrame(dataset)

# Auto-label using our rule-based logic (this is how we generate ground truth)
def label_entry(row):
    score = 0
    if row.sleep_hours < 5: score += 30
    elif row.sleep_hours < 6.5: score += 20
    elif row.sleep_hours < 7.5: score += 10

    mood_map = {1: 30, 2: 22, 3: 14, 4: 6, 5: 0}
    score += mood_map.get(row.mood_score, 0)

    if row.tasks_completion_rate < 0.3: score += 25
    elif row.tasks_completion_rate < 0.6: score += 15
    elif row.tasks_completion_rate < 0.8: score += 7

    if row.days_in_stress >= 5: score += 15
    elif row.days_in_stress >= 3: score += 8
    elif row.days_in_stress >= 1: score += 3

    if score >= 60: return 2    # red
    elif score >= 35: return 1  # amber
    return 0                    # green

df["label"] = df.apply(label_entry, axis=1)

# Features and target
X = df[["sleep_hours", "mood_score", "tasks_completion_rate", "days_in_stress"]]
y = df["label"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(n_estimators=100, max_depth=4, random_state=42, eval_metric='mlogloss')
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("\n✅ Model trained successfully!\n")
print(classification_report(y_test, y_pred, target_names=["green", "amber", "red"]))

# Feature importance
print("📊 Feature Importance:")
for name, score in zip(X.columns, model.feature_importances_):
    print(f"   {name}: {round(score * 100, 1)}%")

# Save model
with open("backend/burnmap_api/predictor/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n💾 Model saved → backend/burnmap_api/predictor/model.pkl")
