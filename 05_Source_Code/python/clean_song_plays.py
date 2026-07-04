from __future__ import annotations

import argparse
import csv
from datetime import datetime
from pathlib import Path
from typing import Iterable


CRITICAL_FIELDS = ("play_id", "user_id", "song_id", "played_at")
EXPECTED_FIELDS = ("play_id", "user_id", "song_id", "played_at", "device", "city")


def parse_timestamp(value: str) -> str:
    """Parse a handful of common timestamp formats and normalize to ISO-like text."""
    value = value.strip()
    formats = (
        "%Y-%m-%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%d-%m-%Y %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
    )
    for fmt in formats:
        try:
            return datetime.strptime(value, fmt).strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            continue
    raise ValueError(f"Unsupported timestamp format: {value}")


def normalize_text(value: str, *, lower: bool = False, title: bool = False) -> str:
    value = value.strip()
    if lower:
        return value.lower()
    if title:
        return value.title()
    return value


def is_missing(row: dict[str, str], field_names: Iterable[str]) -> bool:
    for field in field_names:
        if not row.get(field, "").strip():
            return True
    return False


def clean_rows(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, int]]:
    seen: set[tuple[str, ...]] = set()
    cleaned: list[dict[str, str]] = []
    removed_duplicates = 0
    removed_missing = 0
    parsed_failures = 0

    for row in rows:
        if is_missing(row, CRITICAL_FIELDS):
            removed_missing += 1
            continue

        try:
            normalized_row = {
                "play_id": str(int(row["play_id"].strip())),
                "user_id": str(int(row["user_id"].strip())),
                "song_id": str(int(row["song_id"].strip())),
                "played_at": parse_timestamp(row["played_at"]),
                "device": normalize_text(row.get("device", ""), lower=True),
                "city": normalize_text(row.get("city", ""), title=True),
            }
        except (ValueError, TypeError):
            parsed_failures += 1
            continue

        row_key = tuple(normalized_row[field] for field in EXPECTED_FIELDS)
        if row_key in seen:
            removed_duplicates += 1
            continue

        seen.add(row_key)
        cleaned.append(normalized_row)

    summary = {
        "rows_before": len(rows),
        "rows_after": len(cleaned),
        "duplicates_removed": removed_duplicates,
        "rows_missing_removed": removed_missing,
        "parse_failures_removed": parsed_failures,
    }
    return cleaned, summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Clean raw song play CSV data.")
    parser.add_argument("--input", required=True, help="Path to the raw CSV file.")
    parser.add_argument("--output", required=True, help="Path to write the cleaned CSV file.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with input_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    cleaned_rows, summary = clean_rows(rows)

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=EXPECTED_FIELDS)
        writer.writeheader()
        writer.writerows(cleaned_rows)

    print("CSV cleaning completed")
    print(f"Rows before cleaning: {summary['rows_before']}")
    print(f"Rows after cleaning:  {summary['rows_after']}")
    print(f"Duplicates removed:   {summary['duplicates_removed']}")
    print(f"Missing rows removed: {summary['rows_missing_removed']}")
    print(f"Parse failures:       {summary['parse_failures_removed']}")
    print(f"Output file:          {output_path}")


if __name__ == "__main__":
    main()
