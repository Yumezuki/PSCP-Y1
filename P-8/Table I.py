"""Table I"""


def table(num):
    """function"""

    last = 1
    while num != last - 1:
        total = 15 * last
        print("15 x %d = %d" % (last, total))
        last += 1


table(int(input()))
