"""Stair"""


def stairs(step, stair):
    """function"""
    count = 0
    tmp = 0
    out = 0
    for _ in range(stair):
        height_stair = int(input())
        tmp = height_stair + tmp
        if height_stair > step:
            out = 1
        elif tmp == step:
            count += 1
            tmp = 0
        elif tmp > step:
            count += 1
            tmp = height_stair
    if tmp > 0:
        count += 1
    if out == 1:
        print("NO")
    else:
        print(count)


stairs(int(input()), int(input()))
