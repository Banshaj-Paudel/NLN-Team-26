import random
import json

random.seed(42)

def generate_entry():
    return {
        "sleep_hours": round(random.uniform(3.5, 9.0), 1),
        "mood_score": random.randint(1, 5),
        "tasks_completion_rate": round(random.uniform(0.1, 1.0), 2),
        "days_in_stress": random.randint(0, 7)
    }

if __name__ == "__main__":
    dataset = [generate_entry() for _ in range(500)]
    with open("mock_dataset.json", "w") as f:
        json.dump(dataset, f, indent=2)
    print(f"✅ Generated {len(dataset)} mock entries → mock_dataset.json")
