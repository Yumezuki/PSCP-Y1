"""PickThemAgain"""


def pick(lst):
    """function"""
    lst_space = lst.split()
    num = 0
    for i in lst_space[::-1]:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            print(i)
            num += 1
    if num == 0:
        print("Nope")


pick(input())
