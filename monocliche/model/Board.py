from monocliche import Constants

from monocliche.model import Box, Deck, Auction

from monocliche.model.actions.GoToBoxAction import GoToBoxAction
from monocliche.model.actions.GoToBoxTypeAction import GoToBoxTypeAction
from monocliche.model.actions.GoToJailAction import GoToJailAction
from monocliche.model.actions.OutOfJailFreeAction import OutOfJailFreeAction
from monocliche.model.actions.StreetRepairsAction import StreetRepairsAction
from monocliche.model.actions.UpdateAmountAction import UpdateAmountAction
from monocliche.model.actions.UpdateAmountEachPlayerAction import UpdateAmountEachPlayerAction
from monocliche.model.actions.UpdatePositionAction import UpdatePositionAction


class Board:

    def __init__(self):
        self.boxes: list[Box] = None
        self.community_chest_deck: Deck = None
        self.chance_deck: Deck = None
        self.auction: Auction = None

    def initialize_board(self):
        """Initialize all the spaces and the two decks on the board"""

        self.__initialize_boxes()
        self.__initialize_community_chest_deck()
        self.__initialize_chance_deck()

    def __initialize_boxes(self):
        self.boxes = [None] * Constants.NUMBER_OF_BOXES

        self.boxes[0] = None
        self.boxes[1] = None
        self.boxes[2] = None
        self.boxes[3] = None
        self.boxes[4] = None
        self.boxes[5] = None
        self.boxes[6] = None
        self.boxes[7] = None
        self.boxes[8] = None
        self.boxes[9] = None
        self.boxes[10] = None
        self.boxes[11] = None
        self.boxes[12] = None
        self.boxes[13] = None
        self.boxes[14] = None
        self.boxes[15] = None
        self.boxes[16] = None
        self.boxes[17] = None
        self.boxes[18] = None
        self.boxes[19] = None
        self.boxes[20] = None
        self.boxes[21] = None
        self.boxes[22] = None
        self.boxes[23] = None
        self.boxes[24] = None
        self.boxes[25] = None
        self.boxes[26] = None
        self.boxes[27] = None
        self.boxes[28] = None
        self.boxes[29] = None
        self.boxes[30] = None
        self.boxes[31] = None
        self.boxes[32] = None
        self.boxes[33] = None
        self.boxes[34] = None
        self.boxes[35] = None
        self.boxes[36] = None
        self.boxes[37] = None
        self.boxes[38] = None
        self.boxes[39] = None

    def __initialize_community_chest_deck(self):
        pass

    def __initialize_chance_deck(self):
        pass
