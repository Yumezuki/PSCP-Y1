"""BookWorm"""


def worm(test):
    """Function"""
    for _ in range(test):
        time = float(input())
        book = sorted([float(input()) for _ in range(int(input()))])
        i = 0
        for i in range(len(book)):
            if sum(book[: i + 1]) > time:
                break
            i += 1
        print(i)


worm(int(input()))
