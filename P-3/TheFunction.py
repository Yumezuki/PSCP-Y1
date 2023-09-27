""""TheFunctionWithin"""


def funf(num):
    """f(x)"""
    return 2 * num


def fung(num):
    """g(x)"""
    return 3 * num**4 - num**3 + 2 * num**2 + 10


def funh(num1, num2, num3):
    """h(x)"""
    return (num3 + num1) ** 2 - num1 * num2 + num2**2


def funi(num1, num2, num3, num4):
    """i(x)"""
    return (num1**2 + num2**2 - num3**2) / (
        num4**2 - 2 * num1 * num4 + 2 * num1
    )


def main(num1, num2, num3, num4):
    """Function Within"""
    print(funf(funf(num1)))
    print(fung(funf(num1 - num2)))
    print(funh(funf(num1 + num2), funf(num1 + num3), fung(funf(num4**2))))

    print(
        funi(
            funh(funf(num1 + num2), funf(num1 - num3), fung(funf(num4**2))),
            fung(funf(num1 - num2)),
            funf(funf(funf(funf(funf(num3))))),
            num4**8,
        )
    )


main(float(input()), float(input()), float(input()), float(input()))
