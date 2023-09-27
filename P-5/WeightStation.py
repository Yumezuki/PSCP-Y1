"""WeightStation"""


def weightstation():
    """function"""
    avr = int(input())
    wei = 0
    num = 0
    for _ in range(3):
        weight = int(input())
        wei += weight
        if weight > (avr / 2) + avr or weight < avr - (avr / 2):
            num += 1
    total = (avr * 4) - wei
    if avr * 4 > 15000:
        print("Overweight")
    elif num > 0:
        print("Unbalance")
    else:
        print("Pass %.2f" % total)


weightstation()
