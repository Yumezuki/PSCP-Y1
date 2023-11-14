"""Socks"""


def sock(socks):
    """Function"""
    check = []
    new = []
    count = 0
    for i in socks:
        check.append(i)
    check.sort()
    while len(check) > 1:
        if check[0] == check[1]:
            new.append(check[0])
            check.remove(check[0])
            check.remove(check[0])
            count += 1
        elif check[0] != check[1]:
            check.remove(check[0])
    if count == 0:
        print("None")
    else:
        print(new)
    print(count)


sock(input())
