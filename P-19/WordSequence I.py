"""WordSequence I"""


def word_sequence(text):
    """function"""
    for i in range(len(text)):
        for j in range(i + 1):
            print(text[j], end="")
        print()


word_sequence(input())
