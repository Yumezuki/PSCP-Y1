"""Sequence IX"""


def sequenceix(num):
    """function"""

    for i in range(0, num):
        rou = 1
        for _ in range(i + 1, num):
            print("  ", end=" ")
        for _ in range(0, i + 1):
            print("%02d" % rou, end=" ")
            rou += 1
        if i != 0:
            rou = i
            for _ in range(0, i):
                print("%02d" % rou, end=" ")
                rou -= 1
        print("\r")


sequenceix(int(input()))
