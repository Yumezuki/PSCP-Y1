"""RockPaperScissor"""


def whoru(win):
    """function"""
    awin = 0
    bwin = 0
    num = 0
    for _ in range(len(win) // 2):
        if win[num : num + 2] in ["RS", "SP", "PR"]:
            awin += 1
        elif win[num : num + 2] in ["SR", "PS", "RP"]:
            bwin += 1
        num += 2
    return awin, bwin


def rps(play):
    """function"""
    awin, bwin = whoru(play)
    if awin == bwin:
        print("DRAW", awin)
    elif awin > bwin:
        print("A win %d-%d" % (awin, bwin))
    elif bwin > awin:
        print("B win %d-%d" % (bwin, awin))


rps(input())
