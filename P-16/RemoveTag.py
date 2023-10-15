"""RemoveTag"""


def retag(tag):
    """Function"""
    tag = tag.replace("<", "?@").replace(">", "@?").split("?")
    lst = []
    want = []
    for i in tag:
        if "@" not in i:
            lst.append(i)
    lst = " ".join(lst).split(" ")
    for i in lst:
        if i != "":
            want.append(i)
    print(want)


retag(input())
