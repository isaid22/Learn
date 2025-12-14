from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Optional, Tuple

# Reuse normalizers from Parse-PDF.py logic (duplicated here for isolation)
DATE_FORMATS = [
    "%B %d, %Y",
    "%b %d, %Y",
    "%Y-%m-%d",
    "%m/%d/%Y",
]


def normalize_date(value: str) -> Optional[str]:
    """
    Normalize a date-like string to ISO format (YYYY-MM-DD).

    - Trims leading/trailing whitespace.
    - Attempts multiple known date formats defined in DATE_FORMATS.
    - Returns the first successful parse as an ISO date string.
    - Returns None if none of the formats match.

    Useful for ETL pipelines and MCP tools needing consistent date values.

    Args:
        value: Raw date string from input.

    Returns:
        ISO date string (YYYY-MM-DD) if parsing succeeds; otherwise None.
    """
    v = value.strip()
    for fmt in DATE_FORMATS:
        try:
            dt = datetime.strptime(v, fmt)
            return dt.date().isoformat()
        except ValueError:
            continue
    return None


def normalize_currency(value: str) -> Optional[Decimal]:
    """
    Normalize a currency-like string to a Decimal.

    - Trims whitespace, removes thousands separators (commas), and strips a leading '$'.
    - Converts to Decimal for precise arithmetic and comparison.
    - Returns None if the value cannot be parsed as a decimal number.

    Args:
        value: Raw currency string (e.g., "$1,000").

    Returns:
        Decimal representation of the amount, or None on parse failure.
    """
    v = value.strip().replace(",", "")
    if v.startswith("$"):
        v = v[1:]
    try:
        return Decimal(v)
    except InvalidOperation:
        return None


def normalize_number(value: str) -> Optional[Decimal]:
    """
    Normalize a generic numeric string to a Decimal.

    - Trims whitespace and removes thousands separators (commas).
    - Converts to Decimal for exact numeric handling.
    - Returns None if parsing fails.

    Args:
        value: Raw numeric string.

    Returns:
        Decimal value or None if invalid.
    """
    v = value.strip().replace(",", "")
    try:
        return Decimal(v)
    except InvalidOperation:
        return None


def normalize_value(term: str, value: str) -> Tuple[Any, str]:
    """
    Normalize an input term/value pair using heuristics.

    - If the term name suggests date, try date normalization.
    - If it suggests currency/amount, try currency normalization.
    - Otherwise attempt date, then generic number, else return cleaned string.

    Args:
        term: Term name (e.g., "Maturity Date", "Stated Principal Amount").
        value: Raw value string.

    Returns:
        (normalized_value, value_type) where value_type is one of
        "date" | "currency" | "number" | "string".
    """
    t = term.lower()
    if "date" in t:
        d = normalize_date(value)
        if d is not None:
            return d, "date"
    if any(k in t for k in ["amount", "principal", "price", "currency"]):
        c = normalize_currency(value)
        if c is not None:
            return c, "currency"
    d = normalize_date(value)
    if d is not None:
        return d, "date"
    n = normalize_number(value)
    if n is not None:
        return n, "number"
    return value.strip(), "string"


def detect_conflicts(normalized: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Detect conflicts among normalized items grouped by term.

    - Groups items by their 'term'.
    - Flags a conflict when multiple distinct normalized values exist for a term.
    - Applies a simple resolution strategy preferring structured types:
      date > currency > number > string.

    Args:
        normalized: A list of dicts with keys term, raw_value, normalized_value, value_type.

    Returns:
        A list of conflict dicts: {term, values, resolution}.
    """
    by_term: Dict[str, List[Dict[str, Any]]] = {}
    for it in normalized:
        by_term.setdefault(it["term"], []).append(it)

    conflicts: List[Dict[str, Any]] = []
    for term, group in by_term.items():
        unique_values = {str(g["normalized_value"]) for g in group}
        if len(unique_values) > 1:
            order = {"date": 3, "currency": 2, "number": 1, "string": 0}
            winner = max(group, key=lambda g: order.get(g["value_type"], 0))
            conflicts.append({
                "term": term,
                "values": [g["raw_value"] for g in group],
                "resolution": f"Resolved to {winner['normalized_value']} ({winner['value_type']})",
            })
    return conflicts


def run_demo_dataset() -> List[Dict[str, str]]:
    """
    Provide a demo dataset containing duplicates and contradictions.

    - Includes equivalent values (duplicates) and differing values (contradictions)
      for both date and currency terms to exercise conflict detection.

    Returns:
        List of raw term/value dicts suitable for feeding into normalization.
    """

    return [
        {"term": "Maturity Date", "value": "December 22, 2028"},
        {"term": "Maturity Date", "value": "12/22/2028"},  # duplicate same logical value
        {"term": "Maturity Date", "value": "2028-12-23"},  # contradiction different date
        {"term": "Stated Principal Amount", "value": "$1,000"},
        {"term": "Stated Principal Amount", "value": "$1000.00"},  # duplicate equivalent
        {"term": "Stated Principal Amount", "value": "$999.99"},   # contradiction
    ]


def main():
    """
    Run the demonstration: normalize values and report conflicts.

    This is a standalone script entry point showing how the helpers can be
    used in an ETL-like workflow or MCP tool. It prints normalized results
    and conflict resolutions to stdout.
    """
    raw = run_demo_dataset()

    normalized: List[Dict[str, Any]] = []
    for item in raw:
        term = item["term"]
        value = item["value"]
        norm, value_type = normalize_value(term, value)
        normalized.append({
            "term": term,
            "raw_value": value,
            "normalized_value": norm,
            "value_type": value_type,
        })

    print("Normalized Terms:")
    for t in normalized:
        print(f"- {t['term']}: raw='{t['raw_value']}' -> {t['normalized_value']} [{t['value_type']}]")

    conflicts = detect_conflicts(normalized)
    if conflicts:
        print("\nConflicts:")
        for c in conflicts:
            print(f"- {c['term']}: inputs={c['values']} | {c['resolution']}")
    else:
        print("\nNo conflicts detected.")


if __name__ == "__main__":
    main()
