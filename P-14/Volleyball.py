"""Volleyball"""


def comp(awin, bwin, val):
    """compare"""
    return awin >= val or bwin >= val


def tied(awin, bwin):
    """tied"""
    return abs(awin - bwin) >= 2


def volley(val, awin=0, bwin=0, team_a=0, team_b=0):
    """volleyball"""
    string = ""
    add = 0
    end_game = False
    while len(val) != 0:
        for i in val:
            if (comp(awin, bwin, 25) and tied(awin, bwin)) and \
                    add <= 3 or (comp(awin, bwin, 15) and tied(awin, bwin) and add == 4):
                end_game = True
                break
            if i == "A":
                awin += 1
            elif i == "B":
                bwin += 1
            string += i
        add += 1
        if awin > bwin:
            team_a += 1
        else:
            team_b += 1
        if add <= 5:
            print("Set %d: A (%d) | B (%d)" % (add, awin, bwin))
        val = val.replace(string, "", 1)
        if add >= 4 and end_game and team_a - team_b != 0 or (abs(team_a - team_b) == 3):
            print("A won %d:%d set" % (team_a, team_b) * (team_a > team_b) + \
                  "B won %d:%d set" % (team_b, team_a) * (team_a < team_b))
            break
        end_game = False
        awin = 0
        bwin = 0
        string = ""
    if not end_game:
        print("The game has not finished yet.")


volley(input() + " ")
