"""Longer"""


def longer(var_r, var_a, var_b):
    """Function"""
    import math as mt

    circle = 2 * mt.pi * var_r
    rectangle = 2 * (var_a + var_b)
    result = abs(circle - rectangle)
    if circle > rectangle:
        print("Circle is longer")
        print("%.5f" % result)
    elif circle < rectangle:
        print("Rectangle is longer")
        print("%.5f" % result)
    else:
        print("Equal")
        print("%.5f" % result)


longer(float(input()), float(input()), float(input()))
