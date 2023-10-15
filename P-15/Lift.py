"""Lift"""


def lift(people, can_weight):
    """Function"""
    result_weight = 0
    txt = ""
    count = 0
    for _ in range(people):
        age = int(input())
        weight = float(input())
        result_weight += weight
        if age < 12 and count != 1:
            txt = "Not Safe"
        else:
            count = 1
            txt = "Safe"
            if txt == "Safe":
                if result_weight <= can_weight:
                    txt = "Safe"
                else:
                    txt = "Not Safe"
    if people == 0:
        print("Safe")
    else:
        print(txt)


lift(int(input()), float(input()))
