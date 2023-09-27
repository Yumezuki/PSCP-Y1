"""ChristmasTree"""


def christmas(leaf, wood):
    """function"""
    for i in range(leaf):
        for _ in range(i, leaf - 1):
            print(" ", end="")
        for _ in range(0, i + 1):
            print("*", end="")
        for _ in range(0, i):
            print("*", end="")
        print()
    for i in range(wood):
        width = ((2 * leaf) - 4) // 2
        for _ in range(width):
            print(" ", end="")
        for _ in range(1):
            print("---", end="")
        print()


christmas(int(input()), int(input()))
