"""Run Length Decoding"""


def run(text):
    """function"""
    text_value = ""
    for word in text:
        if word.isnumeric():
            text_value += word
        else:
            print(word * int(text_value), end="")
            text_value = ""


run(input())
