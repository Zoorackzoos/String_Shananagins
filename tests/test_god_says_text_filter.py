import random
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from god_says_text_filter import (
    get_god_says_string_based_on_randomized_enum_indicators,
    randomized_noun,
    randomized_verb,
    randomized_word,
)


class GodSaysTextFilterTests(unittest.TestCase):
    def setUp(self):
        self.words = {
            "randomized_noun": ["owl"],
            "randomized_verb": ["fly"],
        }

    def test_expands_static_and_category_tokens(self):
        result = get_god_says_string_based_on_randomized_enum_indicators(
            ["The ", randomized_noun, " can ", randomized_verb, "."], self.words
        )
        self.assertEqual(result, "The owl can fly.")

    def test_randomized_word_uses_any_populated_category(self):
        result = get_god_says_string_based_on_randomized_enum_indicators(
            [randomized_word], self.words, random.Random(1)
        )
        self.assertIn(result, {"owl", "fly"})

    def test_missing_category_has_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "randomized_verb"):
            get_god_says_string_based_on_randomized_enum_indicators([randomized_verb], {"randomized_noun": ["owl"]})


if __name__ == "__main__":
    unittest.main()
