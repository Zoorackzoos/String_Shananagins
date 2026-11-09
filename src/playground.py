import random

from text_filters.god_says_text_filter import (
    get_god_says_string_based_on_randomized_enum_indicators,
    configure_word_bank,
    load_word_bank,
    randomized_adjective,
    randomized_interjection,
    randomized_noun,
    randomized_verb,
    randomized_word,
)
path_to_weird_txt_file = "../sheets/grady_ward_sheet/mobypos.txt"
path_to_json_file = "../sheets/grady_ward_sheet/moby_word_bank.json"

configure_word_bank(load_word_bank(
    path=path_to_json_file
))

def print_god_says_string(
        tab_amount="\t"
):
    print(tab_amount,"src/playground.py --> playground --> start")
    inner_tab_amount = "\t" + tab_amount

    god_says_input_array = ["God says: "]

    for i in range(random.randint(0, 100)):
        god_says_input_array.append(randomized_word)
        god_says_input_array.append(" ")

    god_says_string = get_god_says_string_based_on_randomized_enum_indicators(input_array=god_says_input_array)
    print(inner_tab_amount,god_says_string)

    print(tab_amount,"src/playground.py --> playground --> end")

if __name__ == '__main__':
    print("src/playground.py --> start")
    tab_amount="\t"

    print_god_says_string(
        tab_amount=tab_amount
               )

    print("src/playground.py --> end")
