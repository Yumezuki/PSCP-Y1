"""Sequence VIII"""


def sequenceviii(num):
    """function"""
    for i in range(0, num):
        for j in range(i + 1, num):
            print("  ", end=" ")
        for j in range(0, i + 1):
            j += 1
            print("%02d" % j, end=" ")
        print("\r")


sequenceviii(int(input()))
