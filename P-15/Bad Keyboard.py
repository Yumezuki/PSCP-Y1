"""Bad Keyboard"""


def bad(txt):
    """Function"""
    new_txt = ""
    for word in txt:
        if word == "i":
            new_txt += word.replace("i", "o")
        elif word == "o":
            new_txt += word.replace("o", "i")
        elif word == "I":
            new_txt += word.replace("I", "O")
        elif word == "O":
            new_txt += word.replace("O", "I")
        else:
            new_txt += word
    print(new_txt)


bad(input())
