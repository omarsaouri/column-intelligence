from loader import get_nlp
import random


def compute_person_entity_ratio(
    values: list[str], entity: str, max_sample_size: int = 1000
) -> float:
    if not values:
        return 0.0

    if len(values) > max_sample_size:
        values = random.sample(values, max_sample_size)

    nlp = get_nlp()
    person_count = 0
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )

    for doc in nlp.pipe(values, batch_size=32):
        if any(ent.label_ == entity for ent in doc.ents):
            person_count += 1
    return person_count / non_null_count
