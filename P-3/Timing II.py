""""Timing"""


def time():
    """function"""
    seconds = int(input())
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    if days < 10000:
        print("%04d:%02d:%02d:%02d" % (days, hours, minutes, seconds))
    else:
        print("ERR_:__:__:__")


time()
