"""Nearer"""


def near(alice, bob, ice_cream):
    """function"""
    if abs(alice - ice_cream) < abs(bob - ice_cream):
        print("Alice", abs(alice - ice_cream))
    elif abs(alice - ice_cream) > abs(bob - ice_cream):
        print("Bob", abs(bob - ice_cream))
    else:
        print("Sundaes", abs(alice - ice_cream))


near(int(input()), int(input()), int(input()))
