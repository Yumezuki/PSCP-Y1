"""PrasomSib"""


def sib(num):
    """function"""
    lst = []
    total = 0
    for i in range(len(num)):
        total += int(num[i])
        if total == 10:
            lst.append(num[:i])
            total = 0
    print(len(lst))


sib(input())
