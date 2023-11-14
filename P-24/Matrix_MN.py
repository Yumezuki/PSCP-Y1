"""Matrix_MN"""


def matrix(row, col):
    """function"""
    lst = []
    tmp = 0
    for _ in range((row * col)):
        num = int(input())
        lst.append(num)
    for _ in range(row):
        for _ in range(col):
            print(lst[tmp], end=" ")
            tmp += 1
        print()


matrix(int(input()), int(input()))
