"""Helloooo"""


def hello(txt):
    """Function"""
    echo = "aeiou"
    value = 0
    txt_echo = []
    for i in range(len(txt) - 1, -1, -1):
        if txt[i] in echo and value == 0:
            txt_back = txt[i] + txt[i] * 3
            value += 1
            txt_echo.append(txt_back)
        else:
            txt_echo.append(txt[i])

    for i in range(len(txt_echo) - 1, -1, -1):
        print(txt_echo[i], end="")


hello(input())
