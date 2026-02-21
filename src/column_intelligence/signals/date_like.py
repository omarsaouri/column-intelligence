from datetime import datetime


def compute_date_parse_success_ratio(values: list[str]) -> float:
    parsed = 0
    if not values:
        return 0.0
    for v in values:
        try:
            datetime.fromisoformat(str(v))
            parsed += 1
        except Exception:
            pass
    return parsed / len(values) if values else 0.0


def compute_year_range_span(values: list[str]) -> float:
    years = []
    for v in values:
        try:
            years.append(int(str(v)[:4]))
        except Exception:
            pass
    return max(years) - min(years) if years else 0


def compute_monotonic_increasing_ratio(values: list[str]) -> float:
    if len(values) < 2:
        return 0.0
    count = sum(1 for i in range(1, len(values)) if values[i] >= values[i - 1])
    return count / (len(values) - 1)


def compute_time_component_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    return sum(1 for v in values if ":" in v) / len(values)
