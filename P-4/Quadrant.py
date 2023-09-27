"""Quadrant"""


def quadrant(num1, num2):
    """function"""
    if num1 == 0 and num2 == 0:
        print("O")
    elif num1 > 0 and num2 > 0:
        print("Q1")
    elif num1 < 0 and num2 > 0:
        print("Q2")
    elif num1 < 0 and num2 < 0:
        print("Q3")
    elif num1 > 0 and num2 < 0:
        print("Q4")
    elif num1 > 0 or num1 < 0 and num2 == 0:
        print("X")
    elif num1 == 0 and num2 > 0 or num2 < 0:
        print("Y")


quadrant(int(input()), int(input()))
