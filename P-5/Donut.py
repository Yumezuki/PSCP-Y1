"""Donut"""


def donut(price, num, free, donutwant):
    """function"""
    test = 0
    pro = num + free
    buypro = donutwant // pro
    if donutwant == 0:
        print("0 0")
    elif donutwant > 0:
        test = pro * buypro
        left = donutwant - test
        if left >= num:
            left = num
            test += pro
        else:
            test += left
        total = (price * buypro * num) + (left * price)
        print("%d %d" % (total, test))


donut(int(input()), int(input()), int(input()), int(input()))
