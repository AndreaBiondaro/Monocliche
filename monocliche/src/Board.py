from typing import Optional

from monocliche.src import Constants

from monocliche.src.Box import Box
from monocliche.src.Deck import Deck
from monocliche.src.Auction import Auction
from monocliche.src.ActionBox import ActionBox
from monocliche.src.Region import Region
from monocliche.src.Station import Station
from monocliche.src.Company import Company
from monocliche.src.Card import Card

from monocliche.src.actions.DrawCardAction import DrawCardAction
from monocliche.src.actions.GoToBoxAction import GoToBoxAction
from monocliche.src.actions.GoToBoxTypeAction import GoToBoxTypeAction
from monocliche.src.actions.GoToJailAction import GoToJailAction
from monocliche.src.actions.OutOfJailFreeAction import OutOfJailFreeAction
from monocliche.src.actions.StreetRepairsAction import StreetRepairsAction
from monocliche.src.actions.UpdateAmountAction import UpdateAmountAction
from monocliche.src.actions.UpdateAmountEachPlayerAction import UpdateAmountEachPlayerAction
from monocliche.src.actions.UpdatePositionAction import UpdatePositionAction


class Board:

    def __init__(self):
        self.boxes: Optional[list[Box]] = None
        self.community_chest_deck: Optional[Deck] = None
        self.chance_deck: Optional[Deck] = None
        self.auction: Optional[Auction] = None

    def initialize_board(self):
        """Initialize all the spaces and the two decks on the board"""

        self.__initialize_boxes()
        self.__initialize_community_chest_deck()
        self.__initialize_chance_deck()

    def __initialize_boxes(self):
        self.boxes = [None] * Constants.NUMBER_OF_BOXES

        go_action = UpdateAmountAction(500)
        community_chest_action = DrawCardAction(self.community_chest_deck)
        chance_action = DrawCardAction(self.chance_deck)
        income_tax_action = UpdateAmountAction(500)
        super_tax_action = UpdateAmountAction(250)
        go_to_jail_action = GoToJailAction()

        # TODO : Indicate the group to which the properties belong

        self.boxes[0] = ActionBox(Constants.NAME_GO_BOX, go_action)
        self.boxes[1] = Region(Constants.NAME_OLD_KENT_ROAD_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[2] = ActionBox(Constants.NAME_COMMUNITY_CHEST_BOX, community_chest_action)
        self.boxes[3] = Region(Constants.NAME_WHITECHAPEL_ROAD_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[4] = ActionBox(Constants.NAME_INCOME_TAX_BOX, income_tax_action)
        self.boxes[5] = Station(Constants.NAME_KING_CROSS_STATION_BOX, 0, 0, 0)
        self.boxes[6] = Region(Constants.NAME_THE_ANGEL_ISLINGTON_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[7] = ActionBox(Constants.NAME_CHANCE_BOX, chance_action)
        self.boxes[8] = Region(Constants.NAME_EUSTON_ROAD_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[9] = Region(Constants.NAME_PENTONVILLE_ROAD_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[10] = Box(Constants.NAME_JUST_VISITING_BOX)
        self.boxes[11] = Region(Constants.NAME_PALL_MALL_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[12] = Company(Constants.NAME_ELECTRIC_COMPANY_BOX, 0, 0)
        self.boxes[13] = Region(Constants.NAME_WHITEHALL_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[14] = Region(Constants.NAME_NORTHUMRLD_AVENUE_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[15] = Station(Constants.NAME_MARYLEBONE_STATION_BOX, 0, 0, 0)
        self.boxes[16] = Region(Constants.NAME_BOW_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[17] = ActionBox(Constants.NAME_COMMUNITY_CHEST_BOX, community_chest_action)
        self.boxes[18] = Region(Constants.NAME_MARLBOROUGH_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[19] = Region(Constants.NAME_VINE_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[20] = Box(Constants.NAME_FREE_PARKING_BOX)
        self.boxes[21] = Region(Constants.NAME_STRAND_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[22] = ActionBox(Constants.NAME_CHANCE_BOX, chance_action)
        self.boxes[23] = Region(Constants.NAME_FLEET_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[24] = Region(Constants.NAME_TRAFALGAR_SQUARE_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[25] = Station(Constants.NAME_FENCHURCH_STATION_BOX, 0, 0, 0)
        self.boxes[26] = Region(Constants.NAME_LEICESTER_SQUARE_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[27] = Region(Constants.NAME_COVENTRY_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[28] = Company(Constants.NAME_WATER_WORKS_BOX, 0, 0)
        self.boxes[29] = Region(Constants.NAME_PICCADILLY_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[30] = ActionBox(Constants.NAME_GO_TO_JAIL_BOX, go_to_jail_action)
        self.boxes[31] = Region(Constants.NAME_REGENT_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[32] = Region(Constants.NAME_OXFORD_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[33] = ActionBox(Constants.NAME_COMMUNITY_CHEST_BOX, community_chest_action)
        self.boxes[34] = Region(Constants.NAME_BOND_STREET_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[35] = Station(Constants.NAME_LIVERPOOL_STATION_BOX, 0, 0, 0)
        self.boxes[36] = ActionBox(Constants.NAME_CHANCE_BOX, chance_action)
        self.boxes[37] = Region(Constants.NAME_PARK_LANE_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.boxes[38] = ActionBox(Constants.NAME_SUPER_TAX_BOX, super_tax_action)
        self.boxes[39] = Region(Constants.NAME_MAYFAIR_BOX, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def __initialize_community_chest_deck(self):
        cards = [None] * Constants.NUMBER_OF_COMMUNITY_CHEST_CARDS

        cards[0] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_OUT_OF_JAIL, OutOfJailFreeAction())
        cards[1] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_WON_SECOND_PRIZE,
                        UpdateAmountAction(200))
        cards[2] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_SALE_OF_STOCK, UpdateAmountAction(50))
        cards[3] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_LIFE_INSURANCE,
                        UpdateAmountAction(100))
        cards[4] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_INCOME_TAX_REFUND,
                        UpdateAmountAction(20))
        cards[5] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_HOLIDAY_FUND, UpdateAmountAction(100))
        cards[6] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_INHERIT, UpdateAmountAction(100))
        cards[7] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_CONSULTANCY_FEE,
                        UpdateAmountAction(25))
        cards[8] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_PAY_HOSPITAL, UpdateAmountAction(-100))
        cards[9] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_BANK_ERROR, UpdateAmountAction(200))
        cards[10] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_PAY_SCHOOL, UpdateAmountAction(-50))
        cards[11] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_DOCTOR_FEE, UpdateAmountAction(-50))
        cards[12] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_YOUR_BIRTHDAY,
                         UpdateAmountEachPlayerAction(10))
        cards[13] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_ADVANCE_TO_GO,
                         GoToBoxAction(self.boxes[0].id))
        cards[14] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_STREET_REPAIR,
                         StreetRepairsAction(40, 115))
        cards[15] = Card(Constants.COMMUNITY_CHEST_CARD_NAME, Constants.CARD_GO_TO_JAIL, GoToJailAction())

        deck = Deck(cards)
        deck.shuffle()
        self.community_chest_deck = deck

    def __initialize_chance_deck(self):
        cards = [None] * Constants.NUMBER_OF_CHANCE_CARDS

        cards[0] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_OUT_OF_JAIL, OutOfJailFreeAction())
        cards[1] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_MAKE_REPAIRS_ON_PROPERTY,
                        StreetRepairsAction(25, 100))
        cards[2] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_SPEEDING_FINE, UpdateAmountAction(-15))
        cards[3] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ELECTED_CHAIRMAN_OF_ROAD,
                        UpdateAmountEachPlayerAction(-50))
        cards[4] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_BACK_THREE_SPACES, UpdatePositionAction(-3))
        cards[5] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_UTILITY,
                        GoToBoxTypeAction(Company))
        cards[6] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_BANK_PAYS, UpdateAmountAction(50))
        cards[7] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_RAILROAD,
                        GoToBoxTypeAction(Station))
        cards[8] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_PAY_POOR_TAX, UpdateAmountAction(-15))
        cards[9] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_FENCHURCH_STATION,
                        GoToBoxAction(self.boxes[25].id))
        cards[10] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_MAYFAIR,
                         GoToBoxAction(self.boxes[39].id))
        cards[11] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_PALL_MALL,
                         GoToBoxAction(self.boxes[11].id))
        cards[12] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_TRAFALGAR_SQUARE,
                         GoToBoxAction(self.boxes[24].id))
        cards[13] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_LOAN_MATURE, UpdateAmountAction(150))
        cards[14] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_GO_TO_JAIL, GoToJailAction())
        cards[15] = Card(Constants.CHANCE_CARD_NAME, Constants.CARD_ADVANCE_TO_RAILROAD,
                         GoToBoxTypeAction(Station))

        deck = Deck(cards)
        deck.shuffle()

        self.chance_deck = deck
