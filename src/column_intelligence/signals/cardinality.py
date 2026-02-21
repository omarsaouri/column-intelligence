import math
from typing import List, Any, Dict
from collections import Counter


def compute_unique_count(values: List[Any]) -> int:
    """Calculate the number of distinct values."""
    if not values:
        return 0
    return len(set(values))


def compute_unique_ratio(values: List[Any]) -> float:
    """Calculate the ratio of unique values to total rows."""
    if not values:
        return 0.0
    total_rows = len(values)
    unique_count = len(set(values))
    return unique_count / total_rows


def compute_duplicate_ratio(values: List[Any]) -> float:
    """Calculate the percentage of repeated (non-unique) values."""
    if not values:
        return 0.0
    total_rows = len(values)
    unique_count = len(set(values))
    # Duplicate count = total - unique
    duplicate_count = total_rows - unique_count
    return duplicate_count / total_rows


def compute_most_frequent_ratio(values: List[Any]) -> float:
    """Calculate the frequency ratio of the most common value."""
    if not values:
        return 0.0
    total_rows = len(values)
    counter = Counter(values)
    most_frequent_count = counter.most_common(1)[0][1]
    return most_frequent_count / total_rows


def compute_entropy(values: List[Any]) -> float:
    """
    Calculate Shannon entropy of value distribution.
    Measures randomness/unpredictability of the data.

    Higher entropy = more random/uniform distribution
    Lower entropy = more predictable/concentrated distribution
    """
    if not values:
        return 0.0

    total_rows = len(values)
    counter = Counter(values)

    entropy = 0.0
    for count in counter.values():
        if count > 0:
            probability = count / total_rows
            # Shannon entropy formula: -Σ p(x) * log2(p(x))
            entropy -= probability * math.log2(probability)

    return entropy


def compute_value_frequencies(values: List[Any]) -> Dict[Any, int]:
    """Get frequency count for each unique value."""
    if not values:
        return {}
    return dict(Counter(values))


def compute_most_frequent_value(values: List[Any]) -> Any:
    """Get the most frequent value and its count."""
    if not values:
        return None, 0
    counter = Counter(values)
    return counter.most_common(1)[0]
