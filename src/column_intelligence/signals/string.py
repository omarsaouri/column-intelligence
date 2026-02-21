"""
String Statistics Module
Provides functions to compute various statistics on string data.
"""

import statistics
from typing import List, Union


def compute_avg_length(values: List[str]) -> float:
    """
    Compute the average length of strings in the list.

    Args:
        values: List of strings to analyze

    Returns:
        Average string length (0.0 if empty list)
    """
    if not values:
        return 0.0
    return sum(len(s) for s in values) / len(values)


def compute_min_length(values: List[str]) -> int:
    """
    Find the shortest string length in the list.

    Args:
        values: List of strings to analyze

    Returns:
        Length of the shortest string (0 if empty list)
    """
    if not values:
        return 0
    return min(len(s) for s in values)


def compute_max_length(values: List[str]) -> int:
    """
    Find the longest string length in the list.

    Args:
        values: List of strings to analyze

    Returns:
        Length of the longest string (0 if empty list)
    """
    if not values:
        return 0
    return max(len(s) for s in values)


def compute_length_std_dev(values: List[str]) -> float:
    """
    Compute the standard deviation of string lengths.
    Measures variation in length across all strings.

    Args:
        values: List of strings to analyze

    Returns:
        Standard deviation of lengths (0.0 if fewer than 2 values)
    """
    if len(values) < 2:
        return 0.0
    lengths = [len(s) for s in values]
    return statistics.stdev(lengths)


def compute_fixed_length_ratio(values: List[str]) -> float:
    """
    Compute the ratio of values that share the same length.
    Returns the proportion of strings that have the most common length.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if empty list)
    """
    if not values:
        return 0.0

    # Count occurrences of each length
    length_counts = {}
    for s in values:
        length = len(s)
        length_counts[length] = length_counts.get(length, 0) + 1

    # Find the most common length count
    max_count = max(length_counts.values())
    return max_count / len(values)


def compute_whitespace_ratio(values: List[str]) -> float:
    """
    Compute the ratio of strings containing whitespace characters.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if empty list)
    """
    if not values:
        return 0.0

    count_with_whitespace = sum(1 for s in values if any(c.isspace() for c in s))
    return count_with_whitespace / len(values)


def compute_uppercase_ratio(values: List[str]) -> float:
    """
    Compute the ratio of strings that are fully uppercase.
    Only counts strings that have at least one alphabetic character
    and all alphabetic characters are uppercase.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if empty list)
    """
    if not values:
        return 0.0

    count_uppercase = 0
    for s in values:
        # Check if string has at least one letter and all letters are uppercase
        alpha_chars = [c for c in s if c.isalpha()]
        if alpha_chars and all(c.isupper() for c in alpha_chars):
            count_uppercase += 1

    return count_uppercase / len(values)


def compute_lowercase_ratio(values: List[str]) -> float:
    """
    Compute the ratio of strings that are fully lowercase.
    Only counts strings that have at least one alphabetic character
    and all alphabetic characters are lowercase.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if empty list)
    """
    if not values:
        return 0.0

    count_lowercase = 0
    for s in values:
        # Check if string has at least one letter and all letters are lowercase
        alpha_chars = [c for c in s if c.isalpha()]
        if alpha_chars and all(c.islower() for c in alpha_chars):
            count_lowercase += 1

    return count_lowercase / len(values)


def compute_digit_char_ratio(values: List[str]) -> float:
    """
    Compute the ratio of characters that are digits across all strings.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if no characters)
    """
    total_chars = sum(len(s) for s in values)
    if total_chars == 0:
        return 0.0

    digit_count = sum(sum(1 for c in s if c.isdigit()) for s in values)
    return digit_count / total_chars


def compute_alpha_char_ratio(values: List[str]) -> float:
    """
    Compute the ratio of characters that are alphabetic across all strings.

    Args:
        values: List of strings to analyze

    Returns:
        Ratio between 0.0 and 1.0 (0.0 if no characters)
    """
    total_chars = sum(len(s) for s in values)
    if total_chars == 0:
        return 0.0

    alpha_count = sum(sum(1 for c in s if c.isalpha()) for s in values)
    return alpha_count / total_chars


# Convenience function to compute all statistics at once
def compute_all_string_statistics(values: List[str]) -> dict:
    """
    Compute all string statistics at once.

    Args:
        values: List of strings to analyze

    Returns:
        Dictionary containing all computed statistics
    """
    return {
        "avg_length": compute_avg_length(values),
        "min_length": compute_min_length(values),
        "max_length": compute_max_length(values),
        "length_std_dev": compute_length_std_dev(values),
        "fixed_length_ratio": compute_fixed_length_ratio(values),
        "whitespace_ratio": compute_whitespace_ratio(values),
        "uppercase_ratio": compute_uppercase_ratio(values),
        "lowercase_ratio": compute_lowercase_ratio(values),
        "digit_char_ratio": compute_digit_char_ratio(values),
        "alpha_char_ratio": compute_alpha_char_ratio(values),
    }
