from column_intelligence.signals.numeric import compute_numeric_ratio


def test_all_numeric():
    values = [1, 2, 3]
    assert compute_numeric_ratio(values) == 1.0


def test_mixed_values():
    values = ["1", "2", "a"]
    assert compute_numeric_ratio(values) == 2 / 3


def test_empty_list():
    assert compute_numeric_ratio([]) == 0.0


def test_null_values():
    values = ["1", None, "3"]
    assert compute_numeric_ratio(values) == 2 / 3
