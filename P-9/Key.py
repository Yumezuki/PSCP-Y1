"""Key"""


def key(idcard):
    """function"""
    lst = []
    txt = ""
    for i in str(idcard):
        lst.append(int(i))
    for i in lst[-3:]:
        txt += str(i) + ""
    total = sum(lst) + (int(txt) * 10)
    if total < 1000:
        total += 1000
    print(str(total)[-4:])


key(input())
