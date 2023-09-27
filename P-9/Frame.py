"""Frame"""


def frame(txt):
    """function"""
    text = "*" + txt + "*"
    und = len(text) * "*"
    print(und + "\n" + text + "\n" + und)


frame(str(input()))
