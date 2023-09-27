"""Stepper II"""


def stepperii(numx, numy):
    """function"""
    if numx > numy:
        for _ in range(0, abs(numx - numy) + 1):
            print(numx)
            numx -= 1
    else:
        for _ in range(0, abs(numx - numy) + 1):
            print(numx)
            numx += 1


stepperii(int(input()), int(input()))
