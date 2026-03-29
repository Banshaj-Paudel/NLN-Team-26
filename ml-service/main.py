from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from predictor import predict_risk

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
