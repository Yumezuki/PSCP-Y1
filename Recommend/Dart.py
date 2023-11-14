"""Dart"""


def dart(num):
    """Function"""
    score = 0
    for _ in range(num):
        point = input().split()
        point_x = int(point[0])
        pointy = int(point[1])
        shoot = (point_x**2 + pointy**2)**0.5
        if shoot <= 2:
            score += 5
        elif shoot <= 4:
            score += 4
        elif shoot <= 6:
            score += 3
        elif shoot <= 8:
            score += 2
        elif shoot <= 10:
            score += 1
    print(score)

dart(int(input()))
