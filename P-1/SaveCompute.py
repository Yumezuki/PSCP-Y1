""""SaveComputeRepeat"""


def save():
    """function"""
    start_here = 492137954293754252786
    milliseconds = start_here
    seconds = milliseconds // 1000
    milliseconds %= 1000
    minutes = seconds // 60
    seconds %= 60
    hours = minutes // 60
    minutes %= 60
    days = hours // 24
    hours %= 24
    print("%d %d %d %d %d" % (days, hours, minutes, seconds, milliseconds))


save()
