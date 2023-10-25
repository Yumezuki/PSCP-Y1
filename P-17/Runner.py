"""Runner"""


def run(distance, runner):
    """Function"""
    lst = []
    battle = []
    for _ in range(runner):
        number = input().split()
        lst.append(number)
    new_lst = lst.copy()
    lst.sort(key=lambda i: float(i[0]), reverse=True)
    for i in lst:
        battle.append((distance - float(i[1])) / float(i[0]))
    print(new_lst.index(lst[battle.index(min(battle))]) + 1)


run(int(input()), int(input()))
