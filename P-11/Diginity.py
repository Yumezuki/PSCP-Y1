"""Diginity"""


def diginity():
    """function"""
    while True:
        num = input()
        if num == "0":
            break
        while len(num) > 1:
            num = str(sum([int(i) for i in num]))
        print(num)


diginity()
