from typing import List, Any, Dict


def compute_row_count(values: List[Any]) -> int:
    """Calculate the total number of rows."""
    if not values:
        return 0
    return len(values)


def compute_non_null_count(values: List[Any]) -> int:
    """Calculate the number of non-missing (non-null) values."""
    if not values:
        return 0
    return sum(1 for v in values if v is not None)


def compute_null_ratio(values: List[Any]) -> float:
    """Calculate the percentage of missing (null) values."""
    if not values:
        return 0.0
    total_rows = len(values)
    null_count = sum(1 for v in values if v is None)
    return null_count / total_rows


def compute_non_null_ratio(values: List[Any]) -> float:
    """Calculate the percentage of valid (non-null) values."""
    if not values:
        return 0.0
    total_rows = len(values)
    non_null_count = sum(1 for v in values if v is not None)
    return non_null_count / total_rows


# HELPER FUNCTIONS


def compute_null_count(values: List[Any]) -> int:
    """Calculate the number of missing (null) values."""
    if not values:
        return 0
    return sum(1 for v in values if v is None)
