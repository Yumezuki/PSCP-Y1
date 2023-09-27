"""test"""


def main(numx, numy, numr, numxn, numyn):
    """function"""
    import math
    if math.sqrt(((numxn-numx)**2) + ((numyn-numy)**2)) <= numr:
        print("True")
    else:
        print("False")


main(float(input()), float(input()), float(input()), float(input()), float(input()))
