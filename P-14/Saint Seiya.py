"""Saint Seiya"""


def seiya(sec, punch, times=0):
    """function"""
    for i in range(2, sec + 1, 2):
        if times < punch:
            if i % 6 == 0:
                times += 1
            elif i % 2 == 0:
                times += 165
        else:
            times += (sec + 1 - i) * 12
            break
    print(times)


seiya(int(input()), int(input()))
