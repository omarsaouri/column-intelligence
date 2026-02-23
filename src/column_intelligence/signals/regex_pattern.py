import re


def compute_email_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    email_count = 0
    for v in values:
        if isinstance(v, str) and email_pattern.match(v):
            email_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return email_count / non_null_count if non_null_count > 0 else 0.0


def compute_phone_number_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    phone_pattern = re.compile(
        r"^\+?(\d{1,3})?[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}(?:[-.\s]?\d{1,4})?(?:\s?(?:x|ext\.?|#)\s?\d{1,6})?$"
    )
    phone_count = 0
    for v in values:
        if isinstance(v, str) and phone_pattern.match(v):
            phone_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return phone_count / non_null_count if non_null_count > 0 else 0.0


def compute_url_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    url_pattern = re.compile(r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}.*$")
    url_count = 0
    for v in values:
        if isinstance(v, str) and url_pattern.match(v):
            url_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return url_count / non_null_count if non_null_count > 0 else 0.0


def compute_uuid_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    uuid_pattern = re.compile(
        r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-8][0-9a-fA-F]{3}-[89abABcCdD][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
    )
    uuid_count = 0
    for v in values:
        if isinstance(v, str) and uuid_pattern.match(v):
            uuid_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return uuid_count / non_null_count if non_null_count > 0 else 0.0


def compute_date_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    date_pattern = re.compile(
        r"^(?:\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])|(?:0?[1-9]|1[0-2])[\/\-](?:0?[1-9]|[12]\d|3[01])[\/\-](?:\d{4}|\d{2})|(?:0?[1-9]|[12]\d|3[01])[\/\-\.](?:0?[1-9]|1[0-2])[\/\-\.](?:\d{4}|\d{2})|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+(?:0?[1-9]|[12]\d|3[01])(?:st|nd|rd|th)?,?\s+\d{4}|\d{8})$"
    )
    date_count = 0
    for v in values:
        if isinstance(v, str) and date_pattern.match(v):
            date_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return date_count / non_null_count if non_null_count > 0 else 0.0


def compute_percentage_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    percentage_pattern = re.compile(r"^[-+]?\d+(\.\d+)?%$")
    percentage_count = 0
    for v in values:
        if isinstance(v, str) and percentage_pattern.match(v):
            percentage_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return percentage_count / non_null_count if non_null_count > 0 else 0.0


def compute_credit_card_pattern_ratio(values: list[str]) -> float:
    if not values:
        return 0.0
    credit_card_pattern = re.compile(r"^\d{13,19}$")
    credit_card_count = 0
    for v in values:
        if isinstance(v, str) and credit_card_pattern.match(v):
            credit_card_count += 1
    non_null_count = sum(
        1 for v in values if v is not None or (isinstance(v, str) and v.strip() != "")
    )
    return credit_card_count / non_null_count if non_null_count > 0 else 0.0
