import re


def normalize_column_name(column: str) -> str:
    """
    Normalizes a column name to lowercase words separated by spaces.

    Handles:
      - snake_case       → "snake case"
      - camelCase        → "camel case"
      - PascalCase       → "pascal case"
      - SCREAMING_SNAKE  → "screaming snake"
      - kebab-case       → "kebab case"
      - mixed__delims    → "mixed delims"
      - "Already Spaced" → "already spaced"
      - "weird  spacing" → "weird spacing"
    """
    # Insert space before uppercase letters that follow lowercase letters or digits (camelCase, PascalCase)
    s = re.sub(r"([a-z\d])([A-Z])", r"\1 \2", column)

    # Insert space before uppercase letters followed by lowercase letters (e.g. "XMLParser" → "XML Parser")
    s = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", s)

    # Replace any non-alphanumeric characters (_, -, ., etc.) with a space
    s = re.sub(r"[^a-zA-Z0-9]+", " ", s)

    # Collapse multiple spaces and strip, then lowercase everything
    return " ".join(s.split()).lower()
