"""Sequence III"""


def sequenceiii(num):
    """function"""
    for i in range(0, num):
        for j in range(i + 1, (num + i) + 1):
            print(j + 1, end=" ")
        print()


sequenceiii(int(input()))
