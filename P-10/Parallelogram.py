"""Parallelogram"""


def parallelogram(text):
    """function"""
    for i in range((len(text) * 2)):
        if i < len(text):
            for _ in range(i, len(text) - 1):
                print(" ", end="")
            for j in range(0, i + 1):
                print(text[j : j + 1], end="")
            print()
        else:
            for j in range(1):
                print(text[i - (len(text) - 1) : len(text)], end="")
            print()


parallelogram(input())
