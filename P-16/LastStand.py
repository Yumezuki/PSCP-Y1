"""LastStand"""


def last(lst):
    """function"""
    import json

    for i in json.loads(lst):
        print(str(i)[-1])


last(input())
