"""Blackjack"""


def blackjack(numcard):
    """Function"""
    result = 0
    cardace = 0
    for _ in range(numcard):
        card = input()
        if card == "A":
            card = card.replace("A", "11")
            cardace += 1
        if card == "J" or card == "Q" or card == "K":
            card = card.replace("J", "10").replace("Q", "10").replace("K", "10")
        result += int(card)
    while result > 21 and cardace > 0:
        result -= 10
        cardace -= 1
    print(result)


blackjack(int(input()))
