"""Lotto"""


def lottory():
    """function"""
    first_prize = input()
    last_two = input()
    front_three_first = input()
    front_three_second = input()
    last_three_first = input()
    last_three_second = input()
    lotto = input()
    balance = 0

    if lotto == first_prize:
        balance += 6000000

    if lotto[-2] == last_two[0] and lotto[-1] == last_two[1]:
        balance += 2000

    if lotto[0] == front_three_first[0] \
        and lotto[1] == front_three_first[1] \
        and lotto[2] == front_three_first[2]:
        balance += 4000
    if lotto[0] == front_three_second[0] \
        and lotto[1] == front_three_second[1] \
        and lotto[2] == front_three_second[2]:
        balance += 4000

    if lotto[-1] == last_three_first[2] \
        and lotto[-2] == last_three_first[1] \
        and lotto[-3] == last_three_first[0]:
        balance += 4000
    if lotto[-1] == last_three_second[2] \
        and lotto[-2] == last_three_second[1] \
        and lotto[-3] == last_three_second[0]:
        balance += 4000

    if int(first_prize) == 0 and (int(lotto) == 999999 or int(lotto) == 1):
        balance += 100000
    elif int(first_prize) == 999999 and (int(lotto) == 0 or int(lotto) == 999998):
        balance += 100000
    elif (int(lotto)) == int(first_prize) + 1 or (int(lotto)) == int(first_prize) - 1:
        balance += 100000

    print(balance)


lottory()
