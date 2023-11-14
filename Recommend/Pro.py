"""Pro"""


def pro(come, pay, per, person):
    """Function"""
    use_pro = (person // come) * pay
    paid = (use_pro + (person % come)) * per
    print(paid)


pro(int(input()), int(input()), int(input()), int(input()))
