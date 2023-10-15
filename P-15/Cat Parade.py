"""Cat Parade"""


def cat_parade():
    """Function"""
    parade = []
    while True:
        cat = input()
        if cat == "END":
            break
        if cat == "IT'S A DOG":
            parade.pop()
            continue
        if ", " in cat:
            for num in range(len(cat.split(", "))):
                parade.append(cat.split(", ")[num])
        else:
            parade.append(cat)
    lst = []
    for nong in sorted(parade):
        if nong not in lst:
            lst.append(nong)
    for nong in lst:
        print(nong, parade.index(nong) + 1, parade.count(nong))


cat_parade()
