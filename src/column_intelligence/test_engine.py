from .engine import ColumnIntelligenceEngine

engine = ColumnIntelligenceEngine()

values = ["hamid", "akram saouri", "kid cudi", "walid berrada"]

result = engine.analyze("customerFullName", values)

print("COLUMN:", result.column_name)
print("TYPE:", result.inferred_type)
print("CONFIDENCE:", result.confidence)

print("\nSignals:")
for k, v in result.signals.items():
    print(k, ":", v)
