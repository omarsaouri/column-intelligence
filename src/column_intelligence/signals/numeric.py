from typing import Any


def compute_numeric_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    numeric_count = 0

    for v in values:
        try:
            float(v)
            numeric_count += 1
        except (ValueError, TypeError):
            continue
    return numeric_count / len(values)


def compute_integer_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    integer_count = 0

    for v in values:
        try:
            int(v)
            integer_count += 1
        except (ValueError, TypeError):
            continue
    return integer_count / len(values)


def compute_float_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    float_count = 0

    for v in values:
        try:
            float(v)
            float_count += 1
        except (ValueError, TypeError):
            continue
    return float_count / len(values)


def compute_positive_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    positive_count = 0

    for v in values:
        try:
            fv = float(v)
            if fv > 0:
                positive_count += 1
        except (ValueError, TypeError):
            continue
    return positive_count / len(values)


def compute_negative_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    negative_count = 0

    for v in values:
        try:
            fv = float(v)
            if fv < 0:
                negative_count += 1
        except (ValueError, TypeError):
            continue
    return negative_count / len(values)


def compute_zero_ratio(values: list[Any]) -> float:
    if not values:
        return 0.0
    zero_count = 0

    for v in values:
        try:
            fv = float(v)
            if fv == 0:
                zero_count += 1
        except (ValueError, TypeError):
            continue
    return zero_count / len(values)
