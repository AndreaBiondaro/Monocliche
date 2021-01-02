from monocliche.model import Box, Deck, Auction


class Board:

    def __init__(self):
        self.boxes: list[Box] = None
        self.community_chest_deck: Deck = None
        self.chance_deck: Deck = None
        self.auction: Auction = None
