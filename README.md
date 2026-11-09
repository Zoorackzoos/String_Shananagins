# String Shananagins

The project includes the original word-reversal experiment in `src/zoorackzoos_text_filter.py` and
a string-template generator in `src/god_says_text_filter.py`.

The generator deliberately does not include a word dataset. Point
`load_word_bank()` at any JSON word lists you want to use. Its keys are the
indicator names, for example:

```json
{
  "randomized_verb": ["jump", "ponder"],
  "randomized_noun": ["cat", "moon"]
}
```

```python
from god_says_text_filter import (
    get_god_says_string_based_on_randomized_enum_indicators,
    configure_word_bank,
    load_word_bank,
    randomized_adjective,
    randomized_interjection,
    randomized_noun,
    randomized_verb,
    randomized_word,
)

configure_word_bank(load_word_bank("my_word_bank.json"))

template = [
    "I'm so tired, I could ", randomized_verb, " a ", randomized_noun,
    " ", randomized_adjective, ". ", randomized_interjection, "!"
]
print(get_god_says_string_based_on_randomized_enum_indicators(template))

god_says_template = ["God says: "] + [randomized_word] * 20
# Add spaces around each randomized word when building a multi-word sentence.
god_says_template = ["God says: "] + sum(([randomized_word, " "] for _ in range(20)), [])
print(get_god_says_string_based_on_randomized_enum_indicators(god_says_template).rstrip())
```

The API accepts the requested spellings `randomized_prepostions` and
`randomized_determinator`, plus correctly spelled aliases. It also accepts the
singular `randomized_interjection` used in the example.

Run its tests from the project folder:

```powershell
python -m unittest discover -s tests
```
