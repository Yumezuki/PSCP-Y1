"""Ball"""


def ball(height):
    """function"""
    ans = -1
    while height >= 0.01:
        height *= 0.6
        ans += 1
    print(ans)


ball(float(input()))
