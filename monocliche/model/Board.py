from monocliche.model import Box, Deck, Auction


class Board:

    def __init__(self):
        self.boxes: list[Box] = None
        self.probability_deck: Deck = None
        self.boxes_unexpected_deck: Deck = None
        self.auction: Auction = None
