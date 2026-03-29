from sentiment import extract_mood_from_text

def get_watch_data(journal_text: str = None):
    """
    In production pulls from:
    - Apple HealthKit / Google Fit (sleep, HRV)
    - Screen Time API (phone usage)
    - Google Calendar (task completion)
    - Optional journal text → sentiment analysis

    For demo: mock watch data + real sentiment if text provided
    """
    # Mock wearable data
    data = {
        "sleep_hours": 4.5,
        "tasks_completion_rate": 0.4,
        "days_in_stress": 3
    }

    # If user typed something, use NLP mood — else use watch inferred mood
    if journal_text:
        sentiment_result = extract_mood_from_text(journal_text)
        data["mood_score"] = sentiment_result["mood_score"]
        data["mood_source"] = "journal_text"
        data["emotion"] = sentiment_result["sentiment"]
    else:
        data["mood_score"] = 2  # inferred from phone usage
        data["mood_source"] = "watch_inferred"
        data["emotion"] = None

    return data
