from collections import namedtuple
from random import randrange


def sattolo_cycle(items) -> None:
    """Sattolo's algorithm."""
    i = len(items)
    while i > 1:
        i = i - 1
        j = randrange(i)  # 0 <= j <= i-1
        items[j], items[i] = items[i], items[j]


# Create a Card namedtuple and a deck of 52 cards
Card = namedtuple("Card", ["number", "suit"])
deck = [Card(number, suit) for number in range(1,14) for suit in ("D", "H", "C", "S")]

# Shuffle the deck
sattolo_cycle(deck)

# Deal N cards
N = 3
print(deck[:N])


