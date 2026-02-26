# loader.py

_nlp = None


def get_nlp():
    global _nlp

    if _nlp is None:
        try:
            import spacy
        except ImportError:
            raise RuntimeError(
                "spaCy not installed. Install with: pip install column-intelligence[nlp]"
            )

        _nlp = spacy.load("en_core_web_md")

    return _nlp
