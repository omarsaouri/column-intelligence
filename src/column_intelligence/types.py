from dataclasses import dataclass
from typing import Dict


@dataclass
class ColumnSignals:
    numeric_ratio: float = 0.0
    unique_ratio: float = 0.0


@dataclass
class ColumnMetadata:
    column_name: str
    inferred_type: str
    confidence: float
    signals: ColumnSignals
