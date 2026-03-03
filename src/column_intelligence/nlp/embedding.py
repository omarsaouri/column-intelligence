import re
from loader import get_nlp, get_anchor_vecs, SEMANTIC_ANCHORS
import numpy as np
from typing import NamedTuple


class SimilarityResult(NamedTuple):
    score: float
    index: int
    word: str


def normalize_column_name(column_name: str) -> str:
    """
    Normalizes a column name to lowercase words separated by spaces.
    """
    s = re.sub(r"([a-z\d])([A-Z])", r"\1 \2", column_name)
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s)
    return " ".join(s.split()).lower()


def get_column_vector(text: str, nlp) -> np.ndarray:
    """
    Normalizes a column name and returns its sentence embedding vector.
    """
    normalized = normalize_column_name(text)
    sentence_vecs = nlp.encode(normalized, convert_to_numpy=True)

    if not sentence_vecs.size:
        raise ValueError(f"No vectors found for column: '{text}'")

    return sentence_vecs


def cosine_similarity(vec_a: np.ndarray, vec_b: np.ndarray) -> float:
    """Computes cosine similarity between two vectors."""
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return float(np.dot(vec_a, vec_b) / (norm_a * norm_b))


def best_category(
    column_vec: np.ndarray,
    anchors: dict[str, np.ndarray],
    model=None,
) -> dict:
    """
    Returns the most similar category to the given column vector.
    """
    max_category = None
    max_similarity = -float("inf")

    for category, anchor_vec in anchors.items():
        similarity = cosine_similarity(column_vec, anchor_vec)
        if similarity > max_similarity:
            max_similarity = similarity
            max_category = category

    return {"Category": max_category, "Score": max_similarity}


column_vec = get_column_vector("user_id", get_nlp())
anchor_vecs = get_anchor_vecs()
result = best_category(column_vec, anchor_vecs)
print(result)
