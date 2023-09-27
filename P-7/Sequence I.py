"""Stepper I"""


def stepperi(num):
    """function"""
    for _ in range(num):
        for j in range(num):
            print(j + 1, end=" ")
        print()


stepperi(int(input()))
