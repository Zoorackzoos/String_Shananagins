"""
Codex made this :-3
Parse Moby Part-of-Speech II into the word-bank format used by this app.

This uses only the Python standard library and reads the source a line at a
time. A word with multiple codes is placed in every applicable category.
"""

from __future__ import annotations

import argparse
import csv
import json
from collections.abc import Iterator
from pathlib import Path


MOBY_TAGS_TO_INDICATORS = {
    "N": ("randomized_noun",), "p": ("randomized_noun",), "h": ("randomized_noun",),
    "V": ("randomized_verb",), "t": ("randomized_verb",), "i": ("randomized_verb",),
    "A": ("randomized_adjective",), "v": ("randomized_adverb",),
    "C": ("randomized_conjunction",), "P": ("randomized_prepositions",),
    "!": ("randomized_interjections",), "r": ("randomized_pronoun",),
    "o": ("randomized_pronoun",), "D": ("randomized_determinator",),
    "I": ("randomized_determinator",),
}
WORD_BANK_KEYS = tuple(dict.fromkeys(category for values in MOBY_TAGS_TO_INDICATORS.values() for category in values))


def parse_mobypos(source: str | Path) -> Iterator[tuple[str, str]]:
    """Yield ``(word, pos_codes)`` records, reporting malformed line numbers."""
    # Moby's original DOS-era distribution contains bytes outside UTF-8.
    # CP437 decodes every byte and matches the original DOS distribution.
    with Path(source).open(encoding="cp437") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.rstrip("\r\n")
            if not line:
                continue
            try:
                word, pos_codes = line.rsplit("\\", maxsplit=1)
            except ValueError as error:
                raise ValueError(f"Malformed Moby POS record on line {line_number}: {line!r}") from error
            if not word or not pos_codes:
                raise ValueError(f"Malformed Moby POS record on line {line_number}: {line!r}")
            yield word, pos_codes


def build_word_bank(source: str | Path) -> dict[str, list[str]]:
    """Create the generator word bank without losing multi-tag words."""
    word_banks = {category: [] for category in WORD_BANK_KEYS}
    seen = {category: set() for category in WORD_BANK_KEYS}
    for word, pos_codes in parse_mobypos(source):
        for tag in pos_codes:
            for category in MOBY_TAGS_TO_INDICATORS.get(tag, ()):
                if word not in seen[category]:
                    word_banks[category].append(word)
                    seen[category].add(word)
    return word_banks


def write_word_bank(source: str | Path, destination: str | Path) -> dict[str, list[str]]:
    """Create JSON ready for ``configure_word_bank``."""
    word_bank = build_word_bank(source)
    with Path(destination).open("w", encoding="utf-8", newline="\n") as file:
        json.dump(word_bank, file, ensure_ascii=False)
    return word_bank


def write_records_csv(source: str | Path, destination: str | Path, delimiter: str = ",") -> None:
    """Optionally write one raw ``word,pos_codes`` record per source line."""
    with Path(destination).open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(("word", "pos_codes"))
        writer.writerows(parse_mobypos(source))


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Moby Part-of-Speech II into this project's JSON word bank.")
    parser.add_argument("source", type=Path, help="Path to mobypos.txt")
    parser.add_argument("destination", type=Path, help="JSON output path")
    parser.add_argument("--records-csv", type=Path, help="Optional raw word/POS CSV output")
    parser.add_argument("--records-tsv", type=Path, help="Optional raw word/POS TSV output")
    args = parser.parse_args()
    word_bank = write_word_bank(args.source, args.destination)
    if args.records_csv:
        write_records_csv(args.source, args.records_csv)
    if args.records_tsv:
        write_records_csv(args.source, args.records_tsv, delimiter="\t")
    print(f"Wrote {args.destination} ({sum(map(len, word_bank.values()))} category memberships).")


if __name__ == "__main__":
    main()
