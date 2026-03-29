import pickle
import os
import numpy as np

# Load trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

LEVEL_MAP = {0: "green", 1: "amber", 2: "red"}
REASON_MAP = {
    "green": "Stress levels manageable. Keep maintaining your current habits.",
    "amber": "Burnout risk building up. You're in the early warning window — act now before it worsens.",
    "red": "Critical stress signals across sleep, mood, and productivity. Immediate recovery needed."
}

def predict_risk(sleep_hours: float, mood_score: int,
                 tasks_completion_rate: float, days_in_stress: int) -> dict:

    features = np.array([[sleep_hours, mood_score, tasks_completion_rate, days_in_stress]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    score = int(round(max(probability) * 100))
    level = LEVEL_MAP[prediction]

    return {
        "risk_level": level,
        "score": score,
        "reason": REASON_MAP[level],
        "feature_importance": {
            "mood_score": "35.8%",
            "sleep_hours": "26.5%",
            "days_in_stress": "19.0%",
            "tasks_completion_rate": "18.7%"
        }
    }

def run_auto_check():
    """
    In production pulls from Apple HealthKit / Google Fit / Calendar.
    For demo: uses mock watch data.
    """
    from data_fetcher import get_watch_data
    data = get_watch_data()
    return predict_risk(
        sleep_hours=data["sleep_hours"],
        mood_score=data["mood_score"],
        tasks_completion_rate=data["tasks_completion_rate"],
        days_in_stress=data["days_in_stress"]
    )


if __name__ == "__main__":
    print(predict_risk(8.0, 5, 0.95, 0))
    print(predict_risk(6.0, 3, 0.5, 3))
    print(predict_risk(4.0, 1, 0.2, 6))
