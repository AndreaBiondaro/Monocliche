from abc import abstractmethod
from typing import Optional

from monocliche import Constants

from monocliche.model.Box import Box
from monocliche.model import Player, DiceRollResult


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
                # TODO: A land can only be mortgaged if the whole group to whom
                # belongs is devoid of constructions. Where there are buildings, they
                # they must be sold to the Bank which will pay them half of their purchase price
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

        if isinstance(self, Region):
            for region in self.property_group:
                if region.has_construction():
                    return True
        else:
            return False
