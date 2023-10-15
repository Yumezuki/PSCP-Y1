"""Bonus"""


def boney(salary, years, month):
    """Function"""
    result = 0
    if month >= 10:
        years += 1
    if (years * salary) > 1000000:
        result = 1000000
    else:
        if (years * salary) > (20 * salary) and (years * salary) >= 5000:
            result = salary * 20
        elif (years * salary) < 5000:
            result = 5000
        else:
            result = salary * years
    print(result)


boney(int(input()), int(input()), int(input()))
