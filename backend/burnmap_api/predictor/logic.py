def predict_risk(sleep_hours: float, mood_score: int,
                 tasks_completion_rate: float, days_in_stress: int) -> dict:
    score = 0

    # Sleep (max 30 pts)
    if sleep_hours < 5:
        score += 30
    elif sleep_hours < 6.5:
        score += 20
    elif sleep_hours < 7.5:
        score += 10

    # Mood (max 30 pts)
    mood_map = {1: 30, 2: 22, 3: 14, 4: 6, 5: 0}
    score += mood_map.get(mood_score, 0)

    # Task completion (max 25 pts)
    if tasks_completion_rate < 0.3:
        score += 25
    elif tasks_completion_rate < 0.6:
        score += 15
    elif tasks_completion_rate < 0.8:
        score += 7

    # Consecutive stress days (max 15 pts)
    if days_in_stress >= 5:
        score += 15
    elif days_in_stress >= 3:
        score += 8
    elif days_in_stress >= 1:
        score += 3

    if score >= 60:
        level = "red"
        reason = "Critical stress signals across sleep, mood, and productivity. Immediate recovery needed."
    elif score >= 35:
        level = "amber"
        reason = "Burnout risk building up. You're in the early warning window — act now before it worsens."
    else:
        level = "green"
        reason = "Stress levels manageable. Keep maintaining your current habits."

    return {"risk_level": level, "score": score, "reason": reason}


if __name__ == "__main__":
    # GREEN
    print(predict_risk(8.0, 5, 0.95, 0))
    # AMBER
    print(predict_risk(6.0, 3, 0.5, 3))
    # RED
    print(predict_risk(4.0, 1, 0.2, 6))


def run_auto_check():
    """
    This is what gets called in the real app.
    No user input needed — data comes from the watch.
    """
    from data_fetcher import get_watch_data
    data = get_watch_data()
    result = predict_risk(
        sleep_hours=data["sleep_hours"],
        mood_score=data["mood_score"],
        tasks_completion_rate=data["tasks_completion_rate"],
        days_in_stress=data["days_in_stress"]
    )
    return result
