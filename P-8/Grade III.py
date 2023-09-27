"""Grade III"""


def gradeiii(grade):
    """function"""
    num = 0
    for _ in range(grade):
        score = float(input())
        if 100 >= score >= 95:
            num += 4
        elif score >= 90:
            num += 3.5
        elif score >= 85:
            num += 3
        elif score >= 80:
            num += 2.5
        elif score >= 75:
            num += 2
        elif score >= 70:
            num += 1.5
        elif score >= 65:
            num += 1
        elif score >= 60:
            num += 0.5
        elif score >= 0:
            num += 0
    print("%.2f" % ((int((num / grade) * 100)) / 100))


gradeiii(int(input()))
