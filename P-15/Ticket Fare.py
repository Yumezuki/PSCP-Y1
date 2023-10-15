"""Ticket Fare"""


def ticket():
    """Function"""
    station = int(input())
    first = int(input())
    rate = int(input())
    second = int(input())
    up_rate = int(input())
    up_rate_up = int(input())
    start = int(input())
    stop = int(input())
    result = rate

    if (stop > station or stop < 1) or (start > station or start < 1):
        result = "Error"

    else:
        if abs(stop - start) - first <= 0:
            result = rate
        else:
            new_temp = abs(stop - start) - first
            if new_temp <= second:
                result += new_temp * up_rate
            else:
                result += up_rate * second
                new_temp = abs(stop - start) - first - second
                result += new_temp * up_rate_up

    print(result)


ticket()
