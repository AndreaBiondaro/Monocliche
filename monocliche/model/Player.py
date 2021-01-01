from uuid import uuid4

from monocliche.model import Property, Exchange


class Player:
    def __init__(self, name: str, budget: int = 0):
        self.__id = uuid4()
        self.name: str = name
        self.budget: int = budget
        self.properties: list[Property] = []
        self.in_jail = False
        self.my_turn = False
        self.position = 0
        self.prison_release_card = False
        self.exchanges: list[Exchange] = []

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False

        return self.__id == other.__id

    def add_property(self, prop: Property):
        if self.properties is None:
            self.properties = []

        self.properties.append(prop)

    def remove_property(self, prop: Property):
        if self.properties is not None:
            self.properties.remove(prop)

    def add_exchange(self, exchange: Exchange):
        if self.exchanges is None:
            self.exchanges = []

        self.exchanges.append(exchange)

    def remove_exchange(self, exchange: Exchange):
        if self.exchanges is not None:
            self.exchanges.remove(exchange)
