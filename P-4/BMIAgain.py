"""BMIAgain"""


def bmiagain(weight, height):
    """function"""
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")


bmiagain(int(input()), int(input()))
