from column_intelligence.signals.numeric import compute_positive_ratio


def test_all_positive():
    values = [1, 2, 3]
    assert compute_positive_ratio(values) == 1.0


def test_all_negative():
    values = ["-1", -2, "-3"]
    assert compute_positive_ratio(values) == 0.0


def test_empty_list():
    assert compute_positive_ratio([]) == 0.0


def test_mixed_values():
    values = ["1", "0", "3", "-4"]
    assert compute_positive_ratio(values) == 0.5


def test_null_values():
    values = ["-1", None, "-3"]
    assert compute_positive_ratio(values) == 0.0
