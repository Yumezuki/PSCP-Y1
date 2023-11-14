"""iPad Air"""


def ipad(color, capacity, connect):
    """Function"""
    check = 0
    total = 0
    check_color = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    if color in check_color:
        check += 1
    if capacity == "64":
        if connect == "Wi-Fi":
            check += 1
            total = 19900
        elif connect == "Wi-Fi + Cellular":
            check += 1
            total = 24400
    elif capacity == "256":
        if connect == "Wi-Fi":
            check += 1
            total = 24900
        elif connect == "Wi-Fi + Cellular":
            check += 1
            total = 29400
    if check == 2:
        print(total)
    else:
        print("Not Available")


ipad(input(), input(), input())
