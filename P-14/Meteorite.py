"""Meteorite"""


def meteorite(weight, split, not_danger, missile=0):
    """meteorite"""
    new_split = split
    if weight >= not_danger:
        missile = 1
    while weight >= not_danger:
        weight /= split
        if weight >= not_danger:
            for _ in range(new_split):
                missile += 1
        new_split *= split
    print(missile)


meteorite(float(input()), int(input()), float(input()))
