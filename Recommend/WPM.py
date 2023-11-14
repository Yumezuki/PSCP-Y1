"""WPM"""


def wpm_kids(num):
    """wpm"""
    txt = ""
    if num < 11:
        txt = "Very Slow"
    elif num >= 11 and num < 21:
        txt = "Slow"
    elif num >= 21 and num < 31:
        txt = "Average"
    elif num >= 31 and num < 41:
        txt = "Fast"
    else:
        txt = "Very Fast"
    return txt


def wpm_adults(num):
    """wpm"""
    txt = ""
    if num < 26:
        txt = "Very Slow"
    elif num >= 26 and num < 36:
        txt = "Slow/Beginner"
    elif num >= 36 and num < 46:
        txt = "Intermediate/Average"
    elif num >= 46 and num < 66:
        txt = "Fast/Advanced"
    elif num >= 66 and num < 81:
        txt = "Very Fast"
    else:
        txt = "Insane"
    return txt


def wpm(age, num):
    """Function"""
    if age == "Kids":
        print(wpm_kids(num))
    elif age == "Adults":
        print(wpm_adults(num))


wpm(input(), int(input()))
