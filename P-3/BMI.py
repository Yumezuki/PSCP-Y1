""""Rectangle"""


def data():
    """function"""
    name = str(input())
    weight = float(input())
    heigh = float(input())
    calculate = weight / ((heigh / 100) ** 2)
    print("%s's  BMI = %0.2f" % (name, calculate))


data()
data()
data()
data()
data()
