from data_fetcher import get_watch_data
from logic import predict_risk

def test_auto_flow():
    print("📡 Fetching data from watch...")
    data = get_watch_data()
    
    print(f"""
    ⌚ Watch Data Received:
    - Sleep Hours       : {data['sleep_hours']}
    - Mood Score        : {data['mood_score']}/5
    - Tasks Completed   : {int(data['tasks_completion_rate'] * 100)}%
    - Days in Stress    : {data['days_in_stress']} days
    """)

    result = predict_risk(
        sleep_hours=data["sleep_hours"],
        mood_score=data["mood_score"],
        tasks_completion_rate=data["tasks_completion_rate"],
        days_in_stress=data["days_in_stress"]
    )

    print(f"""
    🔥 BurnMap Result:
    - Risk Level : {result['risk_level'].upper()}
    - Score      : {result['score']}/100
    - Reason     : {result['reason']}
    """)

if __name__ == "__main__":
    test_auto_flow()
