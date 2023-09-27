"""Day I"""


def dayi(days):
    """function"""
    if days % 400 == 0 or days % 4 == 0 and days % 100 != 0:
        print("Yes")
    else:
        print("No")


dayi(int(input()))
