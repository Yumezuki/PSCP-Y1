"""Harshad Number"""


def sum_num(num):
    """cal"""
    total = 0
    if num < 0:
        for i in str(num)[1:]:
            total += int(i)
        total *= -1
    else:
        for i in str(num):
            total += int(i)
    return total


def harshad():
    """function"""
    for _ in range(10):
        num = int(input())
        if num == 0:
            print("No")
        elif len(str(num)) == 1:
            if num % num == 0:
                print("Yes")
            else:
                print("No")
        else:
            if num % sum_num(num) == 0:
                print("Yes")
            else:
                print("No")


harshad()
