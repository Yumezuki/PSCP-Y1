"""Difference"""


def difference(set_a, set_b):
    """function"""
    value = set()
    for _ in range(set_a):
        value.add(int(input()))
    for _ in range(set_b):
        value.discard(int(input()))
    for i in sorted(value):
        print(i, end=" ")


difference(int(input()), int(input()))
