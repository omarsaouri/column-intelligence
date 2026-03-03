from semantic_anchors import SEMANTIC_ANCHORS

import numpy as np

_nlp = None
_anchor_vecs = None


def get_nlp():
    global _nlp, _anchor_vecs

    if _nlp is None:
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError:
            raise RuntimeError(
                "sentence-transformers not installed. Install with: pip install column-intelligence[nlp]"
            )

        _nlp = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        _anchor_vecs = build_anchor_vectors(_nlp)

    return _nlp


def get_anchor_vecs():
    """Returns cached anchor vectors, initializing them if needed."""
    if _anchor_vecs is None:
        get_nlp()
    return _anchor_vecs


def build_anchor_vectors(nlp) -> dict[str, np.ndarray]:
    """
    Builds a single mean vector per category based on the terms in SEMANTIC_ANCHORS.
    """
    category_vecs = {}

    for category, terms in SEMANTIC_ANCHORS.items():
        if terms:
            vecs = nlp.encode(terms, convert_to_numpy=True)  # encodes all terms at once
            category_vecs[category] = np.mean(vecs, axis=0)

    return category_vecs


print(get_anchor_vecs())
