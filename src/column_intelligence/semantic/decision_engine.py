from .weights import WEIGHTS
from .scoring import compute_score


def decide_column_type(signals: dict):
    scores = {}
    for semantic_type in WEIGHTS.keys():
        score = compute_score(semantic_type, signals)
        scores[semantic_type] = score

    best_type = max(scores, key=scores.get)

    return {
        "predicted_type": best_type,
        "confidence": scores[best_type],
        "scores": scores,
    }
