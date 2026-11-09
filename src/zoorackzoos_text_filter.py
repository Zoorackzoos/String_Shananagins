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
        if text[i] == " ":
            word = text[substring_start:i]
            return_string += word[::-1] + " "
            substring_start = i+1

        if i == len(text)-1:
            word = text[substring_start:]
            return_string += word[::-1]

    return return_string

if __name__ == "__main__":
    tab_amount = "\t"
    print("start of Zoorackzoos_sentence_text_filter program")
    user_input = input(tab_amount+"please neter your sentence:")
    print()
    print(Zoorackzoos_sentence_text_filter(text=user_input))
    #print()
    #print(Zoorackzoos_sentence_text_filter(text="hello from hell"))
    print()
    print("end of Zoorackzoos_sentence_text_filter program")