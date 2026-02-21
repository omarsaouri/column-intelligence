import math
from typing import List, Optional


def _to_numeric(values: List[str]) -> List[float]:
    """Helper function to convert string values to numeric (float)."""
    numeric_values = []
    for v in values:
        try:
            numeric_values.append(float(v))
        except (ValueError, TypeError):
            continue
    return numeric_values


def compute_mean(values: List[str]) -> float:
    """Calculate the average value of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    return sum(numeric) / len(numeric)


def compute_median(values: List[str]) -> float:
    """Calculate the middle value of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    sorted_values = sorted(numeric)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    return sorted_values[mid]


def compute_variance(values: List[str]) -> float:
    """Calculate the variance (variability measure) of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    n = len(numeric)
    mean = sum(numeric) / n
    return sum((x - mean) ** 2 for x in numeric) / n


def compute_std_dev(values: List[str]) -> float:
    """Calculate the standard deviation of numeric data."""
    variance = compute_variance(values)
    return math.sqrt(variance)


def compute_min_value(values: List[str]) -> float:
    """Calculate the minimum value of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    return min(numeric)


def compute_max_value(values: List[str]) -> float:
    """Calculate the maximum value of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    return max(numeric)


def compute_range(values: List[str]) -> float:
    """Calculate the range (max - min) of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0
    return max(numeric) - min(numeric)


def compute_skewness(values: List[str]) -> float:
    """Calculate the asymmetry of distribution (skewness) of numeric data."""
    numeric = _to_numeric(values)
    if len(numeric) < 3:
        return 0.0

    n = len(numeric)
    mean = sum(numeric) / n
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric) / n)

    if std_dev == 0:
        return 0.0

    # Fisher-Pearson coefficient of skewness (adjusted for bias)
    skew_sum = sum((x - mean) ** 3 for x in numeric)
    skewness = (n * skew_sum) / ((n - 1) * (n - 2) * std_dev**3)
    return skewness


def compute_kurtosis(values: List[str]) -> float:
    """Calculate the tail heaviness (kurtosis) of numeric data."""
    numeric = _to_numeric(values)
    if len(numeric) < 4:
        return 0.0

    n = len(numeric)
    mean = sum(numeric) / n
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in numeric) / n)

    if std_dev == 0:
        return 0.0

    # Excess kurtosis (Fisher definition: normal distribution = 0)
    kurt_sum = sum((x - mean) ** 4 for x in numeric)
    kurtosis = (n * (n + 1) * kurt_sum) / ((n - 1) * (n - 2) * (n - 3) * std_dev**4)
    kurtosis -= (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
    return kurtosis


def compute_percentile_25(values: List[str]) -> float:
    """Calculate the 25th percentile (first quartile) of numeric data."""
    return _compute_percentile(values, 25)


def compute_percentile_50(values: List[str]) -> float:
    """Calculate the 50th percentile (second quartile / median) of numeric data."""
    return _compute_percentile(values, 50)


def compute_percentile_75(values: List[str]) -> float:
    """Calculate the 75th percentile (third quartile) of numeric data."""
    return _compute_percentile(values, 75)


def _compute_percentile(values: List[str], percentile: float) -> float:
    """Helper function to calculate a specific percentile of numeric data."""
    numeric = _to_numeric(values)
    if not numeric:
        return 0.0

    sorted_values = sorted(numeric)
    n = len(sorted_values)

    # Linear interpolation method
    rank = (percentile / 100) * (n - 1)
    lower_idx = int(math.floor(rank))
    upper_idx = int(math.ceil(rank))

    if lower_idx == upper_idx:
        return sorted_values[lower_idx]

    fraction = rank - lower_idx
    return (
        sorted_values[lower_idx] * (1 - fraction) + sorted_values[upper_idx] * fraction
    )
