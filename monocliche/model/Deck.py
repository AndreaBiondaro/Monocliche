from typing import List

from monocliche.model import Card


class Deck:

    def __init__(self):
        self._cards = None

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, cards: List[Card]):
        self._cards = cards
