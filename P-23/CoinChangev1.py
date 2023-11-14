"""CoinChangev1"""


def coin_change(money):
    """Function"""
    coin = 0
    while True:
        if money == 0:
            break
        elif money - 25 >= 0:
            money = money - 25
            coin += 1
        elif money - 10 >= 0:
            money = money - 10
            coin += 1
        elif money - 5 >= 0:
            money = money - 5
            coin += 1
        elif money - 1 >= 0:
            money = money - 1
            coin += 1
    print(coin)


coin_change(int(input()))
