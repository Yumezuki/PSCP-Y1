""""Regulation"""


def reg():
    """function"""
    num = int(input())
    flo = float(input())
    ste = str(input())
    print("%30d" % num)
    print("%030d" % num)
    print("%0.2f" % flo)
    print("%0.12f" % flo)
    print("%40s" % ste)


reg()
