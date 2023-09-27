"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""


def num(numx, numy, numz):
    """function"""
    if numx < numy and numx < numz:
        if numy < numz:
            return numx, numy, numz
        else:
            return numx, numz, numy

    elif numy < numx and numy < numz:
        if numx < numz:
            return numy, numx, numz
        else:
            return numy, numz, numx

    elif numz < numx and numz < numy:
        if numx < numy:
            return numz, numx, numy
        else:
            return numz, numy, numx
    else:
        return numx, numy, numz


def plan(text, numx, numy, numz):
    """function"""
    numx, numy, numz = num(numx, numy, numz)
    if text.lower() == "ascend":
        print("%.2f, %.2f, %.2f" % (numx, numy, numz))
    elif text.lower() == "descend":
        print("%.2f, %.2f, %.2f" % (numz, numy, numx))


plan(str(input()), float(input()), float(input()), float(input()))
