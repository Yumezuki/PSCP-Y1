"""Bill"""


def bill(total):
    """Function"""
    service = total * 0.1
    if service < 50:
        service = 50
    elif service > 1000:
        service = 1000
    res = total + service
    result = res + ((res) * 0.07)
    print("%.2f" % result)


bill(int(input()))
