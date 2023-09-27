"""Circular I"""


def circulari(numxi, numyi, numr, numxii, numyii):
    """function"""
    import math

    if math.sqrt(((numxii - numxi) ** 2) + ((numyii - numyi) ** 2)) <= numr:
        print("Yes")
    else:
        print("No")


circulari(
    float(input()), float(input()), float(input()), float(input()), float(input())
)
