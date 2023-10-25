"""Diamond I"""


def diamond(value_m, value_n):
    """Function"""
    value = []
    cost = []
    for _ in range(value_m):
        dig = input().split()
        value.append(dig)
    for i in range(value_n):
        num = 0
        for j in value:
            num += int(j[i])
        cost.append(num)
    print(max(cost))


diamond(int(input()), int(input()))
