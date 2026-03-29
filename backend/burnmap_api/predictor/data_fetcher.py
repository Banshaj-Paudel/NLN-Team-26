def get_watch_data():
    """
    In production this would pull from:
    - Apple HealthKit / Google Health Connect (sleep, HRV)
    - Screen Time API (phone usage, typing cadence)
    - Google Calendar / Notion (task completion)
    
    For demo: returns realistic mock data as if fetched from a watch
    """
    return {
        "sleep_hours": 4.5,           # Apple Watch - last night's sleep
        "mood_score": 2,              # inferred from phone usage patterns
        "tasks_completion_rate": 0.4, # Google Calendar - meetings attended
        "days_in_stress": 3           # auto calculated from history
    }
