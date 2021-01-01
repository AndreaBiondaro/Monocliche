from monocliche.model import Card


class Deck:

    def __init__(self, cards=None):
        self.cards: list[Card] = cards
