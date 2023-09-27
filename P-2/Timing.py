""""Timing"""


def time():
    """function"""
    timing = int(input())
    seconds = timing
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    print("%d %d %d %d" % (days, hours, minutes, seconds))


time()
