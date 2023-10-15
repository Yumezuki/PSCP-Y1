"""Squid Game"""


def squid(total_a=0, total_b=0):
    """function"""
    for _ in range(10):
        total_a += int(input())
    for _ in range(10):
        total_b += int(input())
    if total_a == total_b:
        print("AB")
    elif total_a > total_b:
        print("B")
    else:
        print("A")


squid()
