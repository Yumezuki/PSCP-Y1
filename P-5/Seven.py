"""Seven"""


def seven(num):
    """function"""
    if num % 4 == 1:
        print(7)
    elif num % 4 == 2:
        print(9)
    elif num % 4 == 3:
        print(3)
    elif num % 4 == 0:
        print(1)


seven(int(input()))
