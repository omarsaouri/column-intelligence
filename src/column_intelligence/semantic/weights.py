WEIGHTS = {
    "person": {
        # --- SpaCy entity signals ---
        "person_entity_ratio": 0.45,
        # --- Semantic column name ---
        "name_similarity_person": 0.25,
        # --- Data profiling ---
        "alphabetic_ratio": 0.10,
        "capitalized_ratio": 0.10,
        "avg_token_count": 0.05,
        # --- Negative cross-penalties ---
        "digit_ratio": -0.10,
        "email_regex_ratio": -0.15,
        "fixed_length_ratio": -0.05,
        "null_ratio": -0.05,
    },
    "location": {
        # --- SpaCy entity signals ---
        "gpe_entity_ratio": 0.45,
        # --- Semantic column name ---
        "name_similarity_location": 0.25,
        # --- Data profiling ---
        "alphabetic_ratio": 0.10,
        "capitalized_ratio": 0.08,
        "avg_char_length": 0.05,
        "unique_ratio": 0.05,
        # --- Negative cross-penalties ---
        "digit_ratio": -0.10,
        "null_ratio": -0.03,
    },
    "email": {
        # --- Data profiling (regex) ---
        "email_regex_ratio": 0.65,
        "special_char_ratio": 0.08,
        "unique_ratio": 0.07,
        "alphabetic_ratio": 0.05,
        # --- Semantic column name ---
        "name_similarity_email": 0.15,
        # --- Negative cross-penalties ---
        "url_regex_ratio": -0.10,
        "digit_ratio": -0.05,
        "null_ratio": -0.05,
    },
    "date": {
        # --- Data profiling (regex/parse) ---
        "date_parse_ratio": 0.50,
        "fixed_length_ratio": 0.10,
        "numeric_ratio": 0.08,
        "special_char_ratio": 0.05,
        "unique_ratio": 0.05,
        # --- Semantic column name ---
        "name_similarity_date": 0.20,
        # --- Negative cross-penalties ---
        "alphabetic_ratio": -0.10,
        "email_regex_ratio": -0.10,
        "currency_symbol_ratio": -0.10,
        "null_ratio": -0.03,
    },
    "phone": {
        # --- Data profiling (regex) ---
        "phone_regex_ratio": 0.55,
        "digit_ratio": 0.15,
        "fixed_length_ratio": 0.10,
        "special_char_ratio": 0.05,
        # --- Semantic column name ---
        "name_similarity_phone": 0.15,
        # --- Negative cross-penalties ---
        "alphabetic_ratio": -0.15,
        "id_pattern_ratio": -0.10,
        "email_regex_ratio": -0.05,
        "null_ratio": -0.05,
    },
    "id": {
        # --- Data profiling ---
        "unique_ratio": 0.20,
        "entropy_score": 0.20,
        "fixed_length_ratio": 0.15,
        "id_pattern_ratio": 0.15,
        "sequential_ratio": 0.10,
        "prefix_pattern_ratio": 0.08,
        "hex_ratio": 0.07,
        # --- Semantic column name ---
        "name_similarity_id": 0.15,
        # --- Negative cross-penalties ---
        "person_entity_ratio": -0.15,
        "phone_regex_ratio": -0.15,
        "alphabetic_ratio": -0.05,
        "null_ratio": -0.10,
    },
    "money": {
        # --- Data profiling ---
        "currency_symbol_ratio": 0.40,
        "numeric_ratio": 0.25,
        "unique_ratio": 0.05,
        # --- Semantic column name ---
        "name_similarity_money": 0.25,
        # --- Negative cross-penalties ---
        "alphabetic_ratio": -0.10,
        "date_parse_ratio": -0.10,
        "boolean_keyword_ratio": -0.05,
        "null_ratio": -0.05,
    },
    "url": {
        # --- Data profiling (regex) ---
        "url_regex_ratio": 0.65,
        "special_char_ratio": 0.08,
        "avg_char_length": 0.05,
        "digit_ratio": 0.02,
        # --- Semantic column name ---
        "name_similarity_url": 0.20,
        # --- Negative cross-penalties ---
        "email_regex_ratio": -0.15,
        "null_ratio": -0.05,
    },
    "boolean": {
        # --- Data profiling ---
        "boolean_keyword_ratio": 0.55,
        "low_cardinality_score": 0.30,
        "entropy_score": -0.10,
        # --- Semantic column name ---
        "name_similarity_boolean": 0.20,
        # --- Negative cross-penalties ---
        "unique_ratio": -0.10,
        "numeric_ratio": -0.10,
        "null_ratio": -0.05,
    },
    "category": {
        # --- Data profiling ---
        "low_cardinality_score": 0.40,
        "alphabetic_ratio": 0.15,
        "entropy_score": -0.10,
        # --- Semantic column name ---
        "name_similarity_category": 0.20,
        # --- Negative cross-penalties ---
        "unique_ratio": -0.15,
        "numeric_ratio": -0.10,
        "boolean_keyword_ratio": -0.10,
        "null_ratio": -0.05,
    },
    "numeric": {
        # --- Data profiling ---
        "numeric_ratio": 0.55,
        "digit_ratio": 0.20,
        "numeric_range_score": 0.08,
        # --- Semantic column name ---
        "name_similarity_numeric": 0.15,
        # --- Negative cross-penalties ---
        "date_parse_ratio": -0.15,
        "currency_symbol_ratio": -0.15,
        "phone_regex_ratio": -0.10,
        "boolean_keyword_ratio": -0.05,
        "null_ratio": -0.03,
    },
}

# ---------------------------------------------------------------------------
# Feature reference — grouped by source function
# ---------------------------------------------------------------------------
#
# ── 1. DATA PROFILING FEATURES ───────────────────────────────────────────
#   Computed purely from the column values statistically.
#
#   REGEX / PARSE
#     email_regex_ratio       — fraction of values matching email regex
#     url_regex_ratio         — fraction of values matching URL regex
#     phone_regex_ratio       — fraction of values matching phone regex
#     date_parse_ratio        — fraction of values parseable as dates
#     id_pattern_ratio        — fraction matching ID patterns (alphanum+dash/underscore)
#     boolean_keyword_ratio   — fraction in {true, false, yes, no, 0, 1, y, n}
#     currency_symbol_ratio   — fraction containing currency symbols ($, €, £, ¥)
#     hex_ratio               — fraction matching hex/UUID patterns
#
#   CHARACTER-LEVEL
#     numeric_ratio           — fraction of values castable to float
#     digit_ratio             — mean fraction of chars that are digits
#     alphabetic_ratio        — mean fraction of chars that are alphabetic
#     capitalized_ratio       — fraction of values that are title-cased
#     special_char_ratio      — mean fraction of chars that are special (@, /, -, etc.)
#
#   STRUCTURAL
#     fixed_length_ratio      — fraction of values sharing the modal string length
#     unique_ratio            — cardinality / row count
#     low_cardinality_score   — 1 - unique_ratio (scaled)
#     null_ratio              — fraction of null/empty values
#     avg_token_count         — mean number of whitespace-split tokens per value
#     avg_char_length         — mean character length per value
#     entropy_score           — Shannon entropy of the value distribution
#     sequential_ratio        — fraction consistent with a monotonic sequence
#     prefix_pattern_ratio    — fraction of values sharing a common prefix
#     numeric_range_score     — plausibility score based on numeric min/max range
#
# ── 2. ENTITY SIGNALS — SpaCy ────────────────────────────────────────────
#   Run spaCy NER on a sample of column values.
#
#     person_entity_ratio     — fraction of values tagged as PERSON
#     gpe_entity_ratio        — fraction of values tagged as GPE or LOC
#
# ── 3. SEMANTIC COLUMN NAME — SentenceTransformer ────────────────────────
#   Embed the column name and compare to type keyword centroids.
#
#     name_similarity_<type>  — cosine similarity of the column name embedding
#                               to the centroid of type-representative keywords.
#                               Example keyword sets:
#                                 person   → ["name", "person", "full name", "employee", "author"]
#                                 location → ["location", "city", "address", "country", "region"]
#                                 email    → ["email", "mail", "e-mail", "contact", "inbox"]
#                                 date     → ["date", "time", "timestamp", "created at", "dob"]
#                                 phone    → ["phone", "mobile", "tel", "contact number", "fax"]
#                                 id       → ["id", "identifier", "uuid", "key", "code"]
#                                 money    → ["price", "amount", "salary", "cost", "revenue"]
#                                 url      → ["url", "link", "website", "href", "uri"]
#                                 boolean  → ["flag", "active", "enabled", "is", "has"]
#                                 category → ["type", "category", "class", "group", "label"]
#                                 numeric  → ["count", "age", "score", "quantity", "number"]
