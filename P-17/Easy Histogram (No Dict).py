"""Easy Histogram (No Dict)"""


def histogram(text):
    """function"""
    lst = []
    value_text = ""
    for i in text:
        lst.append(i)
    lst.sort()
    for i in lst:
        value = lst.count(i)
        value_text += i + " = " + str(value) + "\n"
    print(value_text)


histogram(input())
