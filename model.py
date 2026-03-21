# model.py
from disease_db import disease_db

def predict(msg: str):
    text = msg.lower()
    best_match = None
    best_score = 0

    # Score each disease by keyword matches
    for entry in disease_db:
        score = 0
        for kw in entry["keywords"]:
            if kw in text:
                score += 1

        if score > best_score:
            best_score = score
            best_match = entry

    # If nothing matches sufficiently, give a generic fallback
    if best_match is None or best_score == 0:
        return "Unknown / Non‑specific condition", ["Consult a healthcare provider"]

    return best_match["disease"], best_match["treatments"]