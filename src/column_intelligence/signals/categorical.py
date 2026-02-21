from collections import Counter
from math import log2


def low_cardinality_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    unique_count = len(set(values))
    return 1.0 - (unique_count / len(values))  # closer to 1 = lower cardinality


def dominant_category_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    counts = Counter(values)
    most_common_count = counts.most_common(1)[0][1]
    return most_common_count / len(values)  # closer to 1 = one value dominates


def category_balance_score(values: list[str]) -> float:
    if not values:
        return 0.0
    counts = Counter(values)
    n_unique = len(counts)
    if n_unique == 1:
        return 0.0  # only one category = perfectly imbalanced
    probs = [c / len(values) for c in counts.values()]
    raw_entropy = -sum(p * log2(p) for p in probs if p > 0)
    max_entropy = log2(n_unique)
    return raw_entropy / max_entropy  # closer to 1 = perfectly balanced
