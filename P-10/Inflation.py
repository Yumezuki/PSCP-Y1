"""Inflation"""


def inflation(price, year):
    """function"""
    price_up = int(price) * 100
    for _ in range(year):
        itr = price_up * 381
        price_up = price_up + itr // 10000
    num_1 = str(price_up)
    num_2 = num_1[-2::]
    num_3 = num_1[::-1]
    num_3 = num_3[2::]
    num_3 = num_3[::-1]
    if num_3 == "":
        num_3 = "0"
    if num_2 == "":
        num_2 = "0"

    print("%d.%02d" % (int(num_3), int(num_2)))


inflation(float(input()), int(input()))
