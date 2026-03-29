import os

import requests


def run_auto_check():
    ml_url = os.getenv("ML_SERVICE_URL", "http://localhost:8000/predict-risk")
    payload = {
        "sleep_hours": 7.0,
        "mood_score": 3,
        "tasks_completion_rate": 0.6,
        "days_in_stress": 2,
    }

    try:
        response = requests.post(ml_url, json=payload, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {
            "risk_level": "amber",
            "score": 42,
            "reason": "Fallback result returned because ML service is unavailable.",
        }
