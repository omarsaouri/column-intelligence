from typing import List
from .types import ColumnMetadata, ColumnSignals
from .signals.orchestrator import compute_all_signals
from .semantic.decision_engine import decide_column_type


class ColumnIntelligenceEngine:
    """
    Core orchestration engine for column type inference.
    """

    def analyze(self, column_name: str, values: List[str]) -> ColumnMetadata:
        """
        Analyze a column and return inferred metadata.
        """
        signals = compute_all_signals(values, column_name)
        decision = decide_column_type(signals)

        return ColumnMetadata(
            column_name=column_name,
            inferred_type=decision["predicted_type"],
            confidence=decision["confidence"],
            signals=decision["scores"],
        )
