"""BootSequence"""


def boot(num):
    """function"""
    nnn = 1
    for _ in range(0, num):
        print(nnn, end="")
        if nnn != num:
            print("_", end="")
        nnn += 1


boot(int(input()))
