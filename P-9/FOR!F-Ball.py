"""FOR!F-Ball"""


def ball(rotate):
    """function"""
    locate = 1
    for i in rotate:
        if i == "A":
            if locate == 1:
                locate = 2
            elif locate == 2:
                locate = 1
        elif i == "B":
            if locate == 2:
                locate = 3
            elif locate == 3:
                locate = 2
        elif i == "C":
            if locate == 1:
                locate = 3
            elif locate == 3:
                locate = 1
    print(locate)


ball(input())
