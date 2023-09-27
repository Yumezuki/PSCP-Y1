"""Sequence VI"""


def sequencevi(num):
    """function"""
    for i in range(num):
        for j in range(i + 1):
            print(j + 1, end=" ")
        print()


sequencevi(int(input()))
