import re
import numpy as np
from typing import NamedTuple

from column_intelligence.signals.nlp.loader import get_anchor_vecs, get_nlp


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
    sentence_vecs = nlp.encode(normalized)

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


def max_cosine(column_vec: np.ndarray, anchors: dict[str, np.ndarray]) -> dict:
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


def compute_name_similarity_signals(
    column_name: str, anchors: dict[str, np.ndarray], nlp
) -> dict[str, float]:
    """
    Computes similarity signals between the column name and predefined semantic anchors.
    Returns a dict mapping 'name_similarity_{category}' -> score, or empty dict on failure.
    """
    # Guard: reject empty or non-string input early
    if not isinstance(column_name, str) or not column_name.strip():
        return "Invalid column name. Must be a non-empty string."

    try:
        column_vec = get_column_vector(column_name, nlp)
        similarity_result = max_cosine(column_vec, anchors)

        category = similarity_result.get("Category")  # use .get() to avoid KeyError
        score = similarity_result.get("Score")

        if category is None or score is None:
            print(f"[DEBUG] Missing keys in similarity_result: {similarity_result}")
            return {}

        result = {f"name_similarity_{category}": score}
        return result

    except ValueError as e:
        print(f"[ERROR] ValueError for column '{column_name}': {e}")
        return {}

    except Exception as e:
        print(
            f"[ERROR] Unexpected error for column '{column_name}': {type(e).__name__}: {e}"
        )
        return {}
