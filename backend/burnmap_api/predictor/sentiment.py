import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from textblob import TextBlob

STRESS_KEYWORDS = [
    "exhausted", "overwhelmed", "burnout", "burnt out", "pressure",
    "can't cope", "stressed", "anxious", "hopeless", "struggling",
    "tired", "drained", "no motivation", "falling behind"
]

NEUTRAL_KEYWORDS = [
    "okay", "ok", "fine", "alright", "average", "normal",
    "nothing special", "so so", "not bad", "decent"
]

def extract_mood_from_text(text: str) -> dict:
    if not text or len(text.strip()) == 0:
        return {"mood_score": 3, "sentiment": "neutral", "source": "default"}

    text_lower = text.lower()
    stress_hit = any(k in text_lower for k in STRESS_KEYWORDS)
    neutral_hit = any(k in text_lower for k in NEUTRAL_KEYWORDS)

    polarity = TextBlob(text).sentiment.polarity  # -1.0 to 1.0

    if neutral_hit and not stress_hit:
        mood_score = 3
        sentiment = "neutral"
    elif stress_hit:
        mood_score = 1
        sentiment = "negative"
    elif polarity >= 0.3:
        mood_score = 5
        sentiment = "positive"
    elif polarity >= 0.1:
        mood_score = 4
        sentiment = "positive"
    elif polarity >= -0.1:
        mood_score = 3
        sentiment = "neutral"
    elif polarity >= -0.3:
        mood_score = 2
        sentiment = "negative"
    else:
        mood_score = 1
        sentiment = "negative"

    return {
        "mood_score": mood_score,
        "sentiment": sentiment,
        "polarity": round(polarity, 2),
        "stress_keywords_detected": stress_hit,
        "source": "journal_text"
    }


if __name__ == "__main__":
    tests = [
        "I've been feeling great today, got a lot done!",
        "I'm exhausted and overwhelmed, nothing is going right",
        "I don't know how much longer I can keep up with this pressure",
        "Had an okay day, nothing special"
    ]

    for text in tests:
        result = extract_mood_from_text(text)
        print(f"\nText     : {text}")
        print(f"Sentiment: {result['sentiment']} (polarity: {result['polarity']})")
        print(f"Stress   : {result['stress_keywords_detected']}")
        print(f"Mood     : {result['mood_score']}/5")
