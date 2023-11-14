"""PongYa"""


def pongya(num):
    """function"""
    if num % 3 == 0 or "3" in str(num)[-1]:
        print("PONG")
    else:
        print(num)


pongya(int(input()))
