"""Sequence II"""


def sequenceii(num):
    """function"""
    stat = 1
    oom = 3
    for _ in range(1, num + 1):
        print(stat, end=" ")
        stat += oom
        oom += 2


sequenceii(int(input()))
