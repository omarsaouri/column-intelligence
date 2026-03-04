from .semantic_anchors import SEMANTIC_ANCHORS

import sys
import threading
import numpy as np

_nlp = None
_anchor_vecs = None
_lock = threading.Lock()


def get_nlp():
    global _nlp, _anchor_vecs

    if _nlp is None:
        with _lock:
            # Double-checked locking to avoid redundant init in race conditions
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


def load_spacy_model():
    # spaCy relies on Pydantic v1 which is incompatible with Python 3.14+
    if sys.version_info >= (3, 14):
        raise RuntimeError(
            f"spaCy is not compatible with Python {sys.version_info.major}.{sys.version_info.minor}. "
            "Please use Python 3.12 or 3.13. "
            "Track spaCy's compatibility at: https://github.com/explosion/spaCy/issues"
        )

    try:
        import spacy
    except ImportError:
        raise RuntimeError(
            "spaCy not installed. Install with: pip install column-intelligence[nlp]"
        )

    try:
        nlp = spacy.load("en_core_web_trf")
    except OSError:
        raise RuntimeError(
            "spaCy model 'en_core_web_trf' not found. Install with: python -m spacy download en_core_web_trf"
        )

    return nlp


def get_anchor_vecs() -> dict[str, np.ndarray]:
    """Returns cached anchor vectors, initializing them if needed."""
    if _anchor_vecs is None:
        get_nlp()

    if _anchor_vecs is None:
        raise RuntimeError(
            "Anchor vectors could not be initialized. Ensure the NLP model loaded successfully."
        )

    return _anchor_vecs


def build_anchor_vectors(nlp) -> dict[str, np.ndarray]:
    """
    Builds a single mean vector per category based on the terms in SEMANTIC_ANCHORS.
    Vectors are L2-normalized so dot product == cosine similarity.
    """
    category_vecs = {}

    for category, terms in SEMANTIC_ANCHORS.items():
        if terms:
            vecs = nlp.encode(terms, convert_to_numpy=True)
            mean_vec = np.mean(vecs, axis=0)

            norm = np.linalg.norm(mean_vec)
            if norm > 0:
                mean_vec = mean_vec / norm

            category_vecs[category] = mean_vec

    return category_vecs
