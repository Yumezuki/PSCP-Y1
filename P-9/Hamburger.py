"""Hamburger"""


def hamburger(left, right):
    """function"""
    pork = (left * 2) + (right * 2)
    print(("|" * left) + ("*" * pork) + ("|" * right))


hamburger(int(input()), int(input()))
