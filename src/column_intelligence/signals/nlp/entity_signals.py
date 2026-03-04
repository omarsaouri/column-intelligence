from .loader import load_spacy_model
import random


def compute_entity_ratio(
    values: list[str], entity: str, max_sample_size: int = 1000
) -> float:
    if not values:
        return 0.0

    if len(values) > max_sample_size:
        values = random.sample(values, max_sample_size)

    nlp = load_spacy_model()
    entity_count = 0

    non_null_count = sum(
        1 for v in values if v is not None and isinstance(v, str) and v.strip() != ""
    )

    for doc in nlp.pipe(values, batch_size=32):
        if any(ent.label_ == entity for ent in doc.ents):
            entity_count += 1
    return entity_count / non_null_count
