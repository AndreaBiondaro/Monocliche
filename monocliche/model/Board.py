from typing import List

from monocliche.model import Box, Deck, Auction


class Board:

    def __init__(self):
        self.boxes = None
        self.probability_deck = None
        self.boxes_unexpected_deck = None
        self.auction = None
