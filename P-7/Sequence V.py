"""Sequence V"""


def sequencev(num):
    """function"""
    for i in range(0, num):
        if i % 7 == 0 and i != 0:
            print()
        print(num, end=" ")
        num -= 1


sequencev(int(input()))
