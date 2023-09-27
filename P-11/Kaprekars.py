"""Kaprekars"""


def calculate_kaprekar(num):
    """Calculate kaprekar"""
    lst = []
    for i in str(num):
        lst.append(int(i))
    value = []
    cal = ""
    while lst:
        text = lst[0]
        for i in lst:
            if i < text:
                text = i
        value.append(text)
        lst.remove(text)
    for i in value:
        cal += str(i)
    return cal


def kaprekars(num):
    """function"""
    count = 1
    while num != "6174":
        if num == "6174":
            print(count)
            break
        if len(str(num)) < 4:
            num = num + "0"
        else:
            sk_number_num = calculate_kaprekar(num)[::-1]
            number = int(sk_number_num) - int(sk_number_num[::-1])
            if number == 6174:
                print(count)
                break
            else:
                num = str(number)
                count = count + 1


kaprekars(int(input()))
