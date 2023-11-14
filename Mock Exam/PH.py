"""PH"""


def measure(value):
    """Function"""

    if value >= 0 and value < 7:
        print("acidic")
    elif value == 7:
        print("neutral")
    elif value > 7 and value <= 14:
        print("akaline")
    else:
        print("error")


measure(float(input()))
