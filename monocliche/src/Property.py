from abc import abstractmethod
from typing import Optional

from monocliche.src import Constants

from monocliche.src.Box import Box
from monocliche.src import Player, DiceRollResult


class Property(Box):
    """
    It manages the behavior of all the squares on the board that can be owned by a player.
    """

    def __init__(self, name: str, price: int, mortgaged_value: int):
        self.price = price
        self.mortgaged_value = mortgaged_value
        self.owner: Optional[Player] = None
        self.__mortgaged = False
        self.property_group: list[Property] = []
        super().__init__(name)

    @abstractmethod
    def calculate_rent(self, dice_roll_result: DiceRollResult) -> int:
        """
        Calculates the rent that the player must give to the player who owns the property.
        """
        pass

    def has_construction(self) -> bool:
        """
        Indicates whether a property has structures.

        :return True if there are any structures that are False otherwise
        """
        return False

    def calculate_sales_value(self) -> int:
        """
        It indicates the value of selling the territory to the bank.
        """
        return self.mortgaged_value

    @property
    def mortgaged(self):
        return self.__mortgaged

    @mortgaged.setter
    def mortgaged(self, mortgaged: bool):
        if not mortgaged:
            # Redeem the property
            if self.__mortgaged:
                self.__mortgaged = False
            else:
                raise Exception(Constants.EXCEPTION_PROPERTY_NOT_MORTGAGED)
        else:
            # Mortgage the property
            if not self.__mortgaged:
                # Check if there are any structures, because before you can proceed with the mortgage
                # you have to sell them
                if self.check_if_properties_have_buildings():
                    raise Exception(Constants.EXCEPTION_SELL_STRUCTURES_BEFORE_PROCEEDING_WITH_ACTION)
                else:
                    self.__mortgaged = True
            else:
                raise Exception(Constants.EXCEPTION_PROPERTY_ALREADY_MORTGAGED)

    def count_properties_owned_by_player(self):
        """
        Returns the number of properties owned by the same player as this property
        """
        counter = 0
        if self.owner is not None:
            for prop in self.property_group:
                if prop.owner == self.owner:
                    counter += 1

        return counter

    def is_group_owned_by_player(self):
        """
        Returns true if the owner of this property owns all properties of the group, otherwise false
        """
        return len(self.property_group) == self.count_properties_owned_by_player()

    def check_if_properties_have_buildings(self) -> bool:
        """Check if there is at least one building for a group property"""

        if self.is_group_owned_by_player():
            for prop in self.property_group:
                if prop.has_construction():
                    return True

        return False

    def check_if_properties_are_mortgaged(self) -> bool:
        """
        Check if a group property is mortgaged.

        :return True if there is a mortgaged property, False otherwise.
        """

        for prop in self.property_group:
            if prop.mortgaged:
                return True

        return False
