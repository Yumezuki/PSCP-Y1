"""SumOfNumber"""


def sumonum(negative):
    """function"""
    total = 0

    while total != negative:
        num = int(input())
        if num == -1:
            break
        else:
            total += num

    print(total)


sumonum(int(input()))
