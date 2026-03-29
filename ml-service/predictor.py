def predict_risk(data):
    score = 0

    # Sleep scoring (max 30 pts)
    if data.sleep_hours < 5:
        score += 30
    elif data.sleep_hours < 6.5:
        score += 20
    elif data.sleep_hours < 7.5:
        score += 10

    # Mood scoring (max 30 pts)
    mood_map = {1: 30, 2: 22, 3: 14, 4: 6, 5: 0}
    score += mood_map.get(data.mood_score, 0)

    # Task completion scoring (max 25 pts)
    if data.tasks_completion_rate < 0.3:
        score += 25
    elif data.tasks_completion_rate < 0.6:
        score += 15
    elif data.tasks_completion_rate < 0.8:
        score += 7

    # Consecutive stress days (max 15 pts)
    if data.days_in_stress >= 5:
        score += 15
    elif data.days_in_stress >= 3:
        score += 8
    elif data.days_in_stress >= 1:
        score += 3

    # Determine level
    if score >= 60:
        level = "red"
        reason = "Critical stress signals across sleep, mood, and productivity. Immediate recovery needed."
    elif score >= 35:
        level = "amber"
        reason = "Burnout risk building up. You're in the early warning window — act now before it worsens."
    else:
        level = "green"
        reason = "Stress levels manageable. Keep maintaining your current habits."

    return {
        "risk_level": level,
        "score": score,
        "reason": reason
    }
