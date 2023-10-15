"""Home Run"""


def run(value, distance):
    """Function"""
    home_run = 0
    for _ in range(value):
        length = float(input())
        if length < distance:
            home_run += 1
    print(home_run)


run(int(input()), float(input()))
