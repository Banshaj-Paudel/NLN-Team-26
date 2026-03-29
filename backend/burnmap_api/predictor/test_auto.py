import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from data_fetcher import get_watch_data
from logic import predict_risk

def test_flow(journal_text=None):
    print(f"\n📝 Journal: '{journal_text or 'None — using watch data'}'")
    data = get_watch_data(journal_text)

    print(f"""
⌚ Data Received:
   Sleep Hours       : {data['sleep_hours']}
   Mood Score        : {data['mood_score']}/5 (from {data['mood_source']})
   Tasks Completed   : {int(data['tasks_completion_rate'] * 100)}%
   Days in Stress    : {data['days_in_stress']} days
    """)

    result = predict_risk(
        sleep_hours=data["sleep_hours"],
        mood_score=data["mood_score"],
        tasks_completion_rate=data["tasks_completion_rate"],
        days_in_stress=data["days_in_stress"]
    )

    print(f"""🔥 BurnMap Result:
   Risk Level : {result['risk_level'].upper()}
   Score      : {result['score']}/100
   Reason     : {result['reason']}
    """)

if __name__ == "__main__":
    # Test 1 - no journal, watch only
    test_flow()

    # Test 2 - with journal text
    test_flow("I'm completely exhausted, I haven't been sleeping and everything feels overwhelming")
