"""String templates with random word-category placeholders.

This module intentionally ships without a vocabulary.  Supply one as a mapping
or load one from JSON with :func:`load_word_bank`.
"""

from __future__ import annotations

import json
import random
from enum import Enum
from pathlib import Path
from typing import Mapping, Sequence


class RandomizedIndicator(str, Enum):
    NOUN = "randomized_noun"
    VERB = "randomized_verb"
    ADJECTIVE = "randomized_adjective"
    ADVERB = "randomized_adverb"
    PRONOUN = "randomized_pronoun"
    PREPOSITIONS = "randomized_prepostions"  # Kept to match the requested API spelling.
    CONJUNCTION = "randomized_conjunction"
    DETERMINER = "randomized_determinator"  # Kept to match the requested API spelling.
    INTERJECTION = "randomized_interjections"
    WORD = "randomized_word"


# Import these names directly when constructing templates, as in the examples.
randomized_noun = RandomizedIndicator.NOUN
randomized_verb = RandomizedIndicator.VERB
randomized_adjective = RandomizedIndicator.ADJECTIVE
randomized_adverb = RandomizedIndicator.ADVERB
randomized_pronoun = RandomizedIndicator.PRONOUN
randomized_prepostions = RandomizedIndicator.PREPOSITIONS
randomized_conjunction = RandomizedIndicator.CONJUNCTION
randomized_determinator = RandomizedIndicator.DETERMINER
randomized_interjections = RandomizedIndicator.INTERJECTION
randomized_word = RandomizedIndicator.WORD

# Sensible aliases for common spelling/singular variations in templates.
randomized_adjetive = randomized_adjective
randomized_prepositions = randomized_prepostions
randomized_determiner = randomized_determinator
randomized_interjection = randomized_interjections


WORD_CATEGORIES = tuple(indicator for indicator in RandomizedIndicator if indicator is not RandomizedIndicator.WORD)
_configured_word_bank: Mapping[str | RandomizedIndicator, Sequence[str]] | None = None


def load_word_bank(path: str | Path) -> dict[str, list[str]]:
    """Load a JSON word bank whose keys are the indicator strings.

    Example: ``{"randomized_verb": ["jump", "dance"]}``.
    """
    with Path(path).open(encoding="utf-8") as file:
        word_bank = json.load(file)
    if not isinstance(word_bank, dict):
        raise ValueError("Word-bank JSON must contain an object of word lists.")
    return {str(category): list(words) for category, words in word_bank.items()}


def configure_word_bank(word_bank: Mapping[str | RandomizedIndicator, Sequence[str]]) -> None:
    """Set the default vocabulary, allowing calls that only pass ``input_array``."""
    global _configured_word_bank
    _configured_word_bank = word_bank


def get_god_says_string_based_on_randomized_enum_indicators(
    input_array: Sequence[str | RandomizedIndicator],
    word_bank: Mapping[str | RandomizedIndicator, Sequence[str]] | None = None,
    rng: random.Random | None = None,
) -> str:
    """Expand a template, retaining static strings exactly as provided.

    ``randomized_word`` selects from every populated category.  Pass ``rng``
    (for example ``random.Random(7)``) when repeatable output is useful.
    """
    chooser = rng if rng is not None else random
    selected_word_bank = word_bank if word_bank is not None else _configured_word_bank
    if selected_word_bank is None:
        raise ValueError("No word bank supplied. Pass word_bank=... or call configure_word_bank() first.")
    normalized_bank = _normalize_word_bank(selected_word_bank)
    output: list[str] = []

    for element in input_array:
        # RandomizedIndicator subclasses str, so check it before plain strings.
        if isinstance(element, RandomizedIndicator):
            output.append(_choose_word(element, normalized_bank, chooser))
        elif isinstance(element, str):
            output.append(element)
        else:
            raise TypeError(f"Template elements must be strings or indicators, got {type(element).__name__}.")
    return "".join(output)


def _normalize_word_bank(word_bank: Mapping[str | RandomizedIndicator, Sequence[str]]) -> dict[RandomizedIndicator, list[str]]:
    normalized: dict[RandomizedIndicator, list[str]] = {}
    for category, words in word_bank.items():
        indicator = category if isinstance(category, RandomizedIndicator) else RandomizedIndicator(category)
        if indicator is RandomizedIndicator.WORD:
            raise ValueError("randomized_word is an indicator, not a word-bank category.")
        usable_words = [word for word in words if isinstance(word, str) and word]
        if usable_words:
            normalized[indicator] = usable_words
    return normalized


def _choose_word(indicator: RandomizedIndicator, word_bank: Mapping[RandomizedIndicator, Sequence[str]], chooser: random.Random) -> str:
    if indicator is RandomizedIndicator.WORD:
        choices = [word for words in word_bank.values() for word in words]
    else:
        choices = list(word_bank.get(indicator, []))
    if not choices:
        raise ValueError(f"No words are available for {indicator.value}.")
    return chooser.choice(choices)
