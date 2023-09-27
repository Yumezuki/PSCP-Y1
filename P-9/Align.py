"""Align"""


def align(size, locate, text):
    """function"""
    if locate == "left":
        txt = size - len(text)
        print(text + (txt * " "))

    elif locate == "center":
        txt = size - len(text)
        dis = txt / 2
        if (dis % 2) != 0:
            let = dis + 0.5
            rig = dis - 0.5
            print((int(let) * " ") + text + (int(rig) * " "))
        else:
            print((int(dis) * " ") + text + (int(dis) * " "))

    elif locate == "right":
        txt = size - len(text)
        print((" " * txt) + text)


align(int(input()), str(input()).lower(), str(input()))
