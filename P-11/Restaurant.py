"""Restaurant"""


def restaurant(pay, promotion, sale, recommend):
    """function"""
    discount = (100 - sale) / 100
    price_sum = pay + recommend
    if price_sum >= promotion:
        price_sum = price_sum * discount
    if pay >= promotion:
        pay = pay * discount
    if pay < price_sum:
        print("No %.3f" % (price_sum - pay))
    elif pay > price_sum:
        print("Yes %.3f" % (pay - price_sum))
    else:
        print("Yes")


restaurant(float(input()), float(input()), float(input()), float(input()))
