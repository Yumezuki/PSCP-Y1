"""Tuple's Sad life"""


def sad_life(txt, txt2):
    """Function"""
    for _ in range(txt.count(txt2)):
        for _ in range(txt.count(txt2)):
            print(txt.index(txt2), end=" ")
        print()


sad_life(tuple(input().split()), input())
