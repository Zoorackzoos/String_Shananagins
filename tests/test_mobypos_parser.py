import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from universal_functions.convert_weird_txt_to_csv_and_json import build_word_bank, write_word_bank


class MobyPosParserTests(unittest.TestCase):
    def test_maps_every_tag_and_preserves_multi_tag_words(self):
        source = Path(__file__).parent / "fixtures" / "mobypos_sample.txt"
        word_bank = build_word_bank(source)
        self.assertEqual(word_bank["randomized_noun"], ["zymolysis", "engineer"])
        self.assertEqual(word_bank["randomized_adjective"], ["zymolysis"])
        self.assertEqual(word_bank["randomized_verb"], ["engineer"])
        self.assertEqual(word_bank["randomized_pronoun"], ["who"])
        self.assertEqual(word_bank["randomized_interjections"], ["hello"])

    def test_writes_loadable_json(self):
        word_bank = build_word_bank(Path(__file__).parent / "fixtures" / "mobypos_sample.txt")
        self.assertEqual(json.loads(json.dumps(word_bank))["randomized_adverb"], ["swiftly"])


if __name__ == "__main__":
    unittest.main()
