"""OTP"""

def word():
    """Function"""
    while True:
        number = input()
        if number == "0":
            break
        number_count = [number.count(str(i)) for i in range(10)]
        if len(number) == 4 and number_count.count(2) == 1:
            print("Valid")
        elif len(number) == 6 and (number_count.count(2) == 2 or number_count.count(3) == 1):
            print("Valid")
        elif len(number) == 8 and (number_count.count(3) == 2 or number_count.count(2) == 3):
            print("Valid")
        else:
            print("Invalid")

word()
