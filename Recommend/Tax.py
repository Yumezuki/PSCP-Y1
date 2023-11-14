"""Tax"""


def tax(use_car, engine):
    """Function"""
    tax_car = 0
    if engine > 1800:
        tax_car += (engine - 1800) * 4
        engine = 1800
    if engine > 600:
        tax_car += (engine - 600) * 1.5
        engine = 600
    tax_car += engine * 0.5

    if use_car == 6:
        tax_car = tax_car * (90 / 100)
    elif use_car == 7:
        tax_car = tax_car * (80 / 100)
    elif use_car == 8:
        tax_car = tax_car * (70 / 100)
    elif use_car == 9:
        tax_car = tax_car * (60 / 100)
    elif use_car >= 10:
        tax_car = tax_car * (50 / 100)
    print("%.2f" % (tax_car))


tax(int(input()), int(input()))
