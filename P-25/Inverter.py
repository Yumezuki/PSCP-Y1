"""Inverter"""


def inverter(txt):
    """Function"""
    new_txt = ""
    for num in txt:
        if num == "0":
            new_txt += "1"
        elif num == "1":
            if "1" not in new_txt:
                new_txt += ""
            else:
                new_txt += "0"
    print(new_txt)


inverter(input())
