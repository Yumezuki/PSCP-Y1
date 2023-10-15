"""PickThem"""


def pick(lst):
    """function"""
    import json

    json.loads(lst)
    num = 0
    for i in json.loads(lst):
        if int(i) % 2 == 0:
            print(i)
            num += 1
    if num == 0:
        print("Nope")


pick(input())
