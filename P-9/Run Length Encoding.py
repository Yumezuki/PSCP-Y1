"""Run Length Encoding"""


def run(text):
    """function"""
    check = text[0]
    num = 0
    text_value = ""
    for i in range(0, len(text)):
        if check == text[i]:
            num += 1
        else:
            text_value += str(num) + text[i - 1]
            check = text[i]
            num = 1
    text_value += str(num) + text[-1]
    print(text_value)


run(input())
