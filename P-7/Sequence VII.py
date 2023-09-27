"""Sequence VII"""


def sequencevii(num):
    """function"""
    for i in range(num):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()
    for i in range(num, 1, -1):
        for j in range(0, i - 1):
            print(j + 1, end=" ")
        print()


sequencevii(int(input()))
