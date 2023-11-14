"""MissingNumber (No Set)"""


def missing_number(num):
    """function"""
    lst_lost = []
    lst = []
    for i in range(1, num + 1):
        lst_lost.append(i)
    while True:
        num_x = int(input())
        if num_x == 0:
            break
        else:
            lst.append(num_x)
    for i in lst:
        if i in lst_lost:
            lst_lost.remove(i)
    lst_lost.sort()
    for i in lst_lost:
        print(i)


missing_number(int(input()))
