"""Phone Number"""


def phone(num, inout):
    """function"""
    if inout == "International":
        num = "+66" + num[1:]
    print(num[:-8], num[-8:-4], num[-4:])


phone(input(), input().title())
