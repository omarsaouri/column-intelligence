from collections import Counter
from math import log2


def compute_constant_length_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    length_counts = Counter(len(v) for v in values)
    most_common_length_count = (
        length_counts.most_common(1)[0][1] if length_counts else 0
    )
    total_count = len(values)
    return most_common_length_count / total_count if total_count > 0 else 0.0


def compute_sequential_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    try:
        parsed_numerics = [int(v) for v in values]
    except ValueError:
        return 0.0

    sequential_count = 0

    for i in range(1, len(parsed_numerics)):
        if parsed_numerics[i] == parsed_numerics[i - 1] + 1:
            sequential_count += 1
            print(f"Sequential pair: {parsed_numerics[i-1]} -> {parsed_numerics[i]}")
            print(f"Current sequential count: {sequential_count}")
    return sequential_count / (len(values) - 1) if len(values) > 1 else 0.0


def compute_no_withspace_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    no_space_count = sum(1 for v in values if " " not in v)
    return no_space_count / len(values)


def compute_high_cardinality_low_entropy_pattern(values: list[str]) -> float:
    if not values:
        return 0.0

    total_count = len(values)

    # cardinality
    counts = Counter(values)
    n_unique = len(counts)
    # entropy
    probs = [count / total_count for count in counts.values()]
    raw_entropy = -sum(p * log2(p) for p in probs if p > 0)
    max_entropy = log2(n_unique) if n_unique > 1 else 1
    normalized_entropy = raw_entropy / max_entropy

    # top-k-coverage
    sorted_counts = sorted(counts.values(), reverse=True)
    cumulative = 0
    n_values_for_coverage = 0
    for c in sorted_counts:
        cumulative += c / total_count
        n_values_for_coverage += 1
        if cumulative >= 0.8:
            break
    coverage_ratio = n_values_for_coverage / n_unique

    is_high_cardinality = n_unique >= 50
    is_low_entropy = normalized_entropy <= 0.6

    return {
        "is_high_cardinality": is_high_cardinality,
        "is_low_entropy": is_low_entropy,
        "normalized_entropy": round(normalized_entropy, 4),
        "concentration_ratio": round(coverage_ratio, 4),
    }
