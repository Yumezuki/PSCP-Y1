""""CompositeFunction"""


def composite():
    """function"""
    num = int(input())
    fgx = 2 * ((num / 2) + 1)
    gfx = ((2 * num) / 2) + 1
    print("%0.2f" % fgx)
    print("%0.2f" % gfx)


composite()
