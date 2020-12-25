from typing import List

from monocliche.model import Box, Deck, Auction


class Board:

    def __init__(self):
        self._boxes = None
        self._probability_deck = None
        self._unexpected_deck = None
        self._auction = None

    @property
    def boxes(self):
        return self._boxes

    @boxes.setter
    def boxes(self, boxes: List[Box]):
        self._boxes = boxes

    @property
    def probability_deck(self):
        return self._probability_deck

    @probability_deck.setter
    def probability_deck(self, probability_deck: Deck):
        self._probability_deck = probability_deck

    @property
    def unexpected_deck(self):
        return self._unexpected_deck

    @unexpected_deck.setter
    def unexpected_deck(self, unexpected_deck: Deck):
        self._unexpected_deck = unexpected_deck

    @property
    def auction(self):
        self._auction

    @auction.setter
    def auction(self, auction: Auction):
        self._auction = auction
