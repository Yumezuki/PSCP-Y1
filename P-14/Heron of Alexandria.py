"""Heron of Alexandria"""


def heron(numx, numy, numz):
    """function"""
    fml = (numx + numy + numz) / 2
    total = (fml * (fml - numx) * (fml - numy) * (fml - numz)) ** 0.5
    print("%.3f" % total)


heron(float(input()), float(input()), float(input()))
