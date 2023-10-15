"""SecondConverter"""


def converter(time, sec, minute, hour):
    """function"""

    mins = time // sec
    seconds = time % sec
    hours = mins // minute
    mins %= minute
    hours %= hour
    print("%d:%d:%d" % (hours, mins, seconds))


converter(int(input()), int(input()), int(input()), int(input()))
