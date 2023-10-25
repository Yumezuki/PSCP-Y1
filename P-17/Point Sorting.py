"""Point Sorting"""


def point(num):
    """Function"""
    for _ in range(num):
        value = int(input())
        lst = []
        for _ in range(value):
            txt = input().split()
            n_lst = []
            n_lst.append(int(txt[0]))
            n_lst.append(int(txt[1]))
            lst.append(n_lst)
        lst.sort(reverse=True, key=lambda lst: lst[1])
        lst.sort(key=lambda lst: lst[0] + lst[1])
        for i in lst:
            for j in i:
                print(j, end=" ")
            print()


point(int(input()))
