"""HowLong"""


def main(value):
    """function"""
    total = 0

    for _ in str(abs(value)):
        total += 1

    print(total)


main(int(input()))
