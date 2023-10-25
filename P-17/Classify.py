"""Classify"""


def classify():
    """Function"""
    stu_id = []
    while True:
        val = input()
        if val == "END":
            break
        stu_id.append(val[:4])
    year = 0
    for i in sorted(set(stu_id)):
        new_year = i[:2]
        print(new_year if new_year != year else "--", int(i[2:4]), stu_id.count(i))
        year = new_year


classify()
