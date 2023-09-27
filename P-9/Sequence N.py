"""Sequence N"""


def sequencen(num):
    """function"""
    for i in range(num):
        for j in range(0, num):
            if j == 0 or j == num - 1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()


sequencen(int(input()))
