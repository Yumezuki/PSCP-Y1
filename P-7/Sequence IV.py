"""Sequence IV"""


def sequenceiv(num):
    """function"""
    num_round = 1
    for i in range(0, num):
        for j in range(i, num + i):
            j = j
            print(num_round, end=" ")
            num_round += 1
        print()


sequenceiv(int(input()))
