"""Milk"""


def milk(price, promotion, bottle, money):
    """function"""
    buy = money // price
    total = buy
    if promotion == 0:
        print(total)
    else:
        while True:
            more = (buy // promotion) * bottle
            total += more
            mod = buy % promotion
            buy = 0
            buy += mod
            buy += more
            more = 0
            if buy < promotion:
                break
        print(total)


milk(int(input()), int(input()), int(input()), int(input()))
