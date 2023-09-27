"""Circular II"""


def circularii(numxi, numyi, numr, numxii, numyii):
    """function"""
    import math

    numrf = float(input())
    if math.sqrt(((numxi - numxii) ** 2) + ((numyi - numyii) ** 2)) < numr + numrf:
        print("Yes")
    else:
        print("No")


circularii(
    float(input()), float(input()), float(input()), float(input()), float(input())
)
