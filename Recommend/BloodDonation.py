"""BloodDonation"""


def blood(age, weight, num, ans=False, doc=False):
    """function"""
    if age == 17 or 60 <= age <= 70:
        doc = input()
    if (age == 17 or 60 <= age <= 70) and doc == "False":
        ans = False
    elif (num == 0 and age > 55) or age < 17 or age > 70 or weight < 45:
        ans = False
    elif (age == 17 or 60 <= age <= 70) and doc == "True" and weight >= 45:
        ans = True
    elif 17 < age < 60 and weight >= 45:
        ans = True
    if ans:
        print("Yes")
    else:
        print("No")


blood(int(input()), int(input()), int(input()))
