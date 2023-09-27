"""Turnstile"""


def turnstile():
    """function"""
    unlock = 0
    people = 0
    while True:
        action = input().lower()
        if action == "end":
            break
        if action == "c":
            unlock = 1
        if action == "p" and unlock == 1:
            people += 1
            unlock = 0
    print(people)


turnstile()
