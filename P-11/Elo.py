"""Elo"""


def elo(num_ra, num_rb, who):
    """function"""
    if who == "A":
        num_e = 1 / (1 + (10 ** ((num_rb - num_ra) / 400)))
    elif who == "B":
        num_e = 1 / (1 + (10 ** ((num_ra - num_rb) / 400)))
    print("%.2f" % num_e)


elo(int(input()), int(input()), input())
