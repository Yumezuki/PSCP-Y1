"""Sequence XII"""


def sequencexii(num):
    """function"""
    for i in range(-num + 1, num, 1):
        for j in range(-num + 1, num, 1):
            print("%02d" % (num - abs(abs(i) - abs(j))), end=" ")
        print()


sequencexii(int(input()))
