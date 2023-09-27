"""FourDirections"""


def four_directions(arrow):
    """function"""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    line_5 = ""
    for i in arrow:
        if i == "U":
            line_1 += "  *   "
            line_2 += " ***  "
            line_3 += "* * * "
            line_4 += "  *   "
            line_5 += "  *   "
        elif i == "D":
            line_1 += "  *   "
            line_2 += "  *   "
            line_3 += "* * * "
            line_4 += " ***  "
            line_5 += "  *   "
        elif i == "L":
            line_1 += "  *   "
            line_2 += " *    "
            line_3 += "***** "
            line_4 += " *    "
            line_5 += "  *   "
        elif i == "R":
            line_1 += "  *   "
            line_2 += "   *  "
            line_3 += "***** "
            line_4 += "   *  "
            line_5 += "  *   "
    print(line_1)
    print(line_2)
    print(line_3)
    print(line_4)
    print(line_5)


four_directions(input())
