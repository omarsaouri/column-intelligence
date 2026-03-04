from typing import List, Dict

from column_intelligence.signals.statistical.alphanumeric import (
    compute_alphanumeric_signals,
)
from column_intelligence.signals.statistical.boolean_binary import (
    compute_boolean_binary_signals,
)
from column_intelligence.signals.statistical.cardinality import (
    compute_cardinality_signals,
)
from column_intelligence.signals.statistical.categorical import (
    compute_categorical_signals,
)
from column_intelligence.signals.statistical.date_like import compute_date_like_signals
from column_intelligence.signals.statistical.distribution import (
    compute_distribution_signals,
)
from column_intelligence.signals.statistical.identifier import (
    compute_identifier_signals,
)
from column_intelligence.signals.statistical.numeric import (
    compute_numeric_signals,
)
from column_intelligence.signals.statistical.regex_pattern import (
    compute_regex_pattern_signals,
)
from column_intelligence.signals.statistical.string import (
    compute_string_signals,
)
from column_intelligence.signals.statistical.structural import (
    compute_structural_signals,
)
from column_intelligence.signals.nlp.entity_signals import compute_entity_ratio


def compute_all_signals(values: List[str], column_name: str) -> Dict[str, float]:
    signals = {}

    signals.update(compute_alphanumeric_signals(values))
    signals.update(compute_boolean_binary_signals(values))
    signals.update(compute_cardinality_signals(values))
    signals.update(compute_categorical_signals(values))
    signals.update(compute_date_like_signals(values))
    signals.update(compute_numeric_signals(values))
    signals.update(compute_identifier_signals(values))
    signals.update(compute_regex_pattern_signals(values))
    signals.update(compute_string_signals(values))
    signals.update(compute_distribution_signals(values))
    signals.update(compute_structural_signals(values))

    for entity in [
        "person",
        "email",
        "phone",
        "location",
        "id",
        "money",
        "url",
        "date",
        "boolean",
        "category",
    ]:

        signals[f"entity_ratio_{entity}"] = compute_entity_ratio(values, entity)

    return signals


print(
    compute_all_signals(["abc", "123", "a1b2", "xyz!", "000-111-222"], "example_column")
)
