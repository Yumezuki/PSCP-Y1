"""Stepper I"""


def stepperi(num):
    """function"""
    for i in range(1, num + 1):
        i = i
        for j in range(1, num + 1):
            print(j, end=" ")
        print()


stepperi(int(input()))
