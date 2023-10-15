"""B - Fully pair?"""


def fully(dancing, val="", alone="", counting=0):
    """function"""
    for i in dancing:
        if val.count(i) <= 0:
            val += i
    for i in val:
        if (int(dancing.count(i)) % 2) == 1:
            counting += 1
            alone += i
    print("fully paired" if counting == 0 else alone)


fully(input().lower())
