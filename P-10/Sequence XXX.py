"""Sequence XXX"""


def sequencexxx(size, num):
    """function"""
    for i in range(size):
        if i == 0 or i == size - 1:
            for _ in range(num):
                print("*" * size, end=" ")
            print()
        else:
            for _ in range(num):
                for j in range(size):
                    if i == j or j == 0 or j == size - 1 or j == size - 1 - i:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("", end=" ")
            print()


sequencexxx(int(input()), int(input()))
