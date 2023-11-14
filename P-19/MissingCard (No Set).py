"""MissingCard (No Set)"""


def missing_card():
    """function"""
    lst = []
    for _ in range(51):
        card = input()
        lst.append(card)

    lst_card = [
        "AS",
        "KS",
        "QS",
        "JS",
        "AH",
        "KH",
        "QH",
        "JH",
        "AD",
        "KD",
        "QD",
        "JD",
        "AC",
        "KC",
        "QC",
        "JC",
    ]
    for i in range(2, 11):
        card_spade = str(i) + "S"
        lst_card.append(card_spade)
    for i in range(2, 11):
        card_heart = str(i) + "H"
        lst_card.append(card_heart)
    for i in range(2, 11):
        card_diamond = str(i) + "D"
        lst_card.append(card_diamond)
    for i in range(2, 11):
        card_club = str(i) + "C"
        lst_card.append(card_club)

    for check in lst:
        if check in lst_card:
            lst_card.remove(check)
    print(lst_card[0])


missing_card()
