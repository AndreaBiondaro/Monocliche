from uuid import uuid4

from monocliche.src import Player, Property


class Exchange:

    def __init__(self, player_from: Player = None, player_to: Player = None, asking_price: int = 0,
                 price_offered: int = 0, required_properties: list[Property] = None,
                 given_properties: list[Property] = None):
        self.__id = uuid4()
        self.player_from: Player = player_from
        self.player_to: Player = player_to
        self.asking_price = asking_price
        self.price_offered = price_offered
        self.required_properties: list[Property] = required_properties
        self.given_properties: list[Property] = given_properties

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Exchange):
            return False

        return self.__id == other.__id
