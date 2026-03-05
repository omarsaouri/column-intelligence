from .weights import WEIGHTS


def compute_score(type_name: str, signals: dict) -> float:
    weights = WEIGHTS.get(type_name, {})
    score = 0.0
    for signal, value in weights.items():
        signal_value = signals.get(signal, 0.0)
        score += signal_value * value

    return score
