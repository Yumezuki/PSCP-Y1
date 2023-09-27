"""Right Arrow"""


def arrow(width, height):
    """function"""
    gap = int((height - 1) / 2)
    for i in range(gap, 0, -1):
        print(" " * (gap - i) + "*" * width)
    print(" " * gap + "*" * width)
    for i in range(gap):
        print(" " * (gap - i - 1) + "*" * width)


arrow(int(input()), int(input()))
