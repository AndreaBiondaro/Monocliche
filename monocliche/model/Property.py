from abc import abstractmethod

from monocliche.model import Box, Player


class Property(Box):

    def __init__(self, name: str, price: int, mortgaged_value: int):
        self._price = price
        self._mortgaged_value: mortgaged_value
        self._owner = None
        self._mortgaged = False
        self._property_group = None
        super().__init__(name)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        self._price = price

    @property
    def mortgaged_value(self):
        return self._mortgaged_value

    @mortgaged_value.setter
    def mortgaged_value(self, mortgaged_value: int):
        self._mortgaged_value = mortgaged_value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner: Player):
        self._owner = owner

    @property
    def mortgaged(self):
        return self._mortgaged

    @mortgaged.setter
    def mortgaged(self, mortgaged: bool):
        self._mortgaged = mortgaged

    @property
    def property_group(self):
        return self._property_group

    @property_group.setter
    def property_group(self, property_group: List[Property]):
        self._property_group = property_group

    @abstractmethod
    def calculate_revenue(self):
        pass
