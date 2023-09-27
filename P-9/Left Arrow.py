"""Left Arrow"""


def arrow(width, hight):
    """function"""
    for i in range(hight):
        blank = hight // 2
        if blank - i >= 0:
            for _ in range(0, blank - i):
                print(" ", end="")
            for _ in range(0, width):
                print("*", end="")
        else:
            for _ in range(0, i - blank):
                print(" ", end="")
            for _ in range(0, width):
                print("*", end="")
        print()


arrow(int(input()), int(input()))
