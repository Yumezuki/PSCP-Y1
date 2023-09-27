""""Math for IT"""


def mfi():
    """function"""
    import math

    num = float(input())
    ara = math.pi * (num**2)
    cir = 2 * math.pi * num
    print("Area: %0.3f" % ara)
    print("Circumference: %0.3f" % cir)


mfi()
