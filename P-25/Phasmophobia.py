"""Phasmophobia"""

def re_ghost(ghost, i):
    """REMOVE"""
    if i in ghost:
        ghost.remove(i)
    return ghost


def ghost_type(lst):
    """GHOST TYPE"""
    ghost = ["Banshee", "Demon", "Jinn", "Mare", "Oni", "Phantom", \
             "Poltergeist", "Revenant", "Shade", "Spirit", "Wraith", \
             "Yurei"]
    if "EMF Level 5" in lst:
        for i in ["Demon", "Mare", "Poltergeist", "Spirit", "Wraith", "Yurei"]:
            ghost = re_ghost(ghost, i)
    if "Ghost Writing" in lst:
        for i in ["Banshee", "Jinn", "Mare", "Phantom", "Poltergeist", "Wraith"]:
            ghost = re_ghost(ghost, i)
    if "Fingerprints" in lst:
        for i in ["Demon", "Jinn", "Mare", "Oni", "Phantom", "Shade", "Yurei"]:
            ghost = re_ghost(ghost, i)
    if "Spirit Box" in lst:
        for i in ["Banshee", "Phantom", "Revenant", "Shade", "Yurei"]:
            ghost = re_ghost(ghost, i)
    if "Freezing Temperatures" in lst:
        for i in ["Jinn", "Oni", "Poltergeist", "Revenant", "Shade", "Spirit"]:
            ghost = re_ghost(ghost, i)
    if "Ghost Orb" in lst:
        for i in ["Banshee", "Demon", "Oni", "Revenant", "Spirit", "Wraith"]:
            ghost = re_ghost(ghost, i)
    return ghost


def phasmo():
    """main"""
    lst = []
    for _ in range(3):
        evi = input()
        lst.append(evi)
    ghost = ghost_type(lst)
    if len(ghost) > 0:
        for i in ghost:
            print(i)
    else:
        print("Not yet discovered")


phasmo()
