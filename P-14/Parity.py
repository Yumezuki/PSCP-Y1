"""Parity"""


def parity(num, text):
    """function"""
    check = 0
    for i in num:
        if i == "1":
            check += 1
    if text == "Even":
        if check % 2 == 0:
            num += "0"
        else:
            num += "1"
    elif text == "Odd":
        if check % 2 == 0:
            num += "1"
        else:
            num += "0"
    print(num)


parity(input(), input())
