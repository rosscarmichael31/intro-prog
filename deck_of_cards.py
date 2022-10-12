from random import randrange


def shuffle(items):
    """
    Shuffle items
    """
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]

    return items


def draw(N, deck):
    """
    Draw a hand of N cards from deck
    """
    hand = []
    for _ in range(N):
        hand.append(deck.pop())

    return hand, deck


def deal_hands(num_players, num_cards, deck):
    """
    Deal cards to each player in turn
    """
    list_of_hands = []
    cards = []
    for i in range(num_players):
        for j in range(num_cards):
            card, deck = draw(1, deck)
            cards.append(card)

        list_of_hands.append(cards)
        cards = []

    return list_of_hands, deck


# Create a deck of cards (list of 52 tuples)
deck = [(number, suit) for number in range(1, 14)
        for suit in ("D", "H", "C", "S")]

# Shuffle the deck
deck = shuffle(deck)

# Deal 6 cards to 4 players
num_players = 4
num_cards = 6

list_of_hands, deck = deal_hands(num_players, num_cards, deck)
