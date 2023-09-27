"""Virus I"""


def virus(vir):
    """function"""

    num = 0
    for i in vir:
        if i == "o":
            num += 1
    print(num)


virus(input())
