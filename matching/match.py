# Dev 4: Anchor matching logic goes here
# Input: user stressor_tags, career_stage
# Output: top 2 anchor matches from DB
anchors = [
    {"id": 1, "name": "Priya S.", "tags": ["final-year-CS", "job-rejection"], "story": "Survived 6 months of rejections, now at Google."},
    {"id": 2, "name": "Arjun M.", "tags": ["startup-stress", "first-job"], "story": "Burned out at my first startup, rebuilt stronger."},
    {"id": 3, "name": "Sara K.", "tags": ["academic-pressure", "final-year-CS"], "story": "Thesis + placement at the same time. Made it out."},
]

def match_anchors(user_tags: list, top_n: int = 2):
    scored = []
    for anchor in anchors:
        overlap = len(set(user_tags) & set(anchor["tags"]))
        scored.append((overlap, anchor))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [a for _, a in scored[:top_n]]

if __name__ == "__main__":
    print(match_anchors(["final-year-CS", "job-rejection"]))
