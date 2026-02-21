def compute_binary_ratio(values: list[str]) -> float:
    valid = {"0", "1", "true", "false", 0, 1, True, False}
    if not values:
        return 0.0
    return sum(1 for v in values if v in valid or str(v).lower() in valid) / len(values)


def compute_distinct_values_count(values: list[str]) -> int:
    if not values:
        return 0.0
    return len(set(values)) <= 2


def compute_boolean_string_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    return sum(1 for v in values if v.lower() in {"true", "false"}) / len(values)
