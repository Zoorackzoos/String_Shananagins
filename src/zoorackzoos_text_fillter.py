def Zoorackzoos_sentence_text_filter_prints(text, tab_amount):
    print(tab_amount,"Zoorackzoos_sentence_text_filter")
    tab_amount += "\t"

    return_string = ""

    substring_start = 0
    #substring_end = len(text)

    print(tab_amount,"entering loop")
    for i in range(len(text)):
        print(tab_amount+"\t",i)
        print(tab_amount+"\t\t",text[i])
        print(tab_amount+"\t\t",text[i] == " ")
        if text[i] == " ":
            print(tab_amount+"\t\t\t word = \""+text[substring_start:i])
            word = text[substring_start:i]
            return_string += word[::-1] + " "
            substring_start = i+1

        if i == len(text)-1:
            word = text[substring_start:]
            return_string += word[::-1]

    print(tab_amount,"return_string -->",return_string)

    return return_string

def Zoorackzoos_sentence_text_filter(text):

    return_string = ""

    substring_start = 0
    for i in range(len(text)):
        if (text[i] == " " or
                text[i] == "." or
                text[i] == "!" or
                text[i] == "," or
                text[i] == "?" or
                text[i] == "\n"):
            word = text[substring_start:i]
            return_string += word[::-1] + text[i]
            substring_start = i+1

        if i == len(text)-1:
            word = text[substring_start:]
            return_string += word[::-1]

    return return_string

if __name__ == "__main__":
    tab_amount = "\t"
    print("start of Zoorackzoos_sentence_text_filter program")
    print(tab_amount+"please enter your sentence. put \"\\0\" to end it:")
    user_input = ""

    end_string_bool = False
    while not end_string_bool:
        new_temp_line = input()
        if new_temp_line == "\\0":
            end_string_bool = True
        else:
            user_input += "\n"+new_temp_line

    print(Zoorackzoos_sentence_text_filter(text=user_input))
    print()
    print("end of Zoorackzoos_sentence_text_filter program")
