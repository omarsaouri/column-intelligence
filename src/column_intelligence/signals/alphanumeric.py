def compute_alphanumeric_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    alphanumeric_count = 0
    for v in values:
        if isinstance(v, str) and v.isalnum():
            alphanumeric_count += 1
    return alphanumeric_count / len(values)


def compute_special_char_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    special_char_count = 0
    for v in values:
        if isinstance(v, str) and any(not c.isalnum() for c in v):
            special_char_count += 1
    return special_char_count / len(values)


def compute_starts_with_digit_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    starts_with_digit_count = 0
    for v in values:
        if isinstance(v, str) and v and v[0].isdigit():
            starts_with_digit_count += 1
    return starts_with_digit_count / len(values)


def compute_ends_with_digit_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    ends_with_digit_count = 0
    for v in values:
        if isinstance(v, str) and v and v[-1].isdigit():
            ends_with_digit_count += 1
    return ends_with_digit_count / len(values)


def compute_contains_symbol_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    contains_symbol_count = 0
    for v in values:
        if isinstance(v, str) and any(not c.isalnum() for c in v):
            contains_symbol_count += 1
    return contains_symbol_count / len(values)


def compute_uuid_pattern_ratio(values: list[str]) -> float:
    import re

    if not values:
        return 0.0
    uuid_pattern = re.compile(
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    )
    uuid_count = 0
    for v in values:
        if isinstance(v, str) and uuid_pattern.match(v):
            uuid_count += 1
    return uuid_count / len(values)


def compute_hex_pattern_ratio(values: list[str]) -> float:
    import re

    if not values:
        return 0.0
    hex_pattern = re.compile(r"^[0-9a-fA-F]+$")
    hex_count = 0
    for v in values:
        if isinstance(v, str) and hex_pattern.match(v):
            hex_count += 1
    return hex_count / len(values)
