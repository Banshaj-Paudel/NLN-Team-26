from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_risk

app = FastAPI()

class CheckIn(BaseModel):
    sleep_hours: float
    mood_score: int        # 1–5
    tasks_completion_rate: float  # 0.0–1.0
    days_in_stress: int    # how many consecutive days flagged

@app.get("/")
def root():
    return {"status": "BurnMap ML service running"}

@app.post("/predict-risk")
def predict(data: CheckIn):
    return predict_risk(data)
