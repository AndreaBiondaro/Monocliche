from abc import abstractmethod

from monocliche.model import Box, Player, Game


class Property(Box.Box):
    """
    It manages the behavior of all the squares on the board that can be owned by a player.
    """

    def __init__(self, name: str, price: int, mortgaged_value: int):
        self.price = price
        self.mortgaged_value = mortgaged_value
        self.owner: Player = None
        self.mortgaged = False
        self.property_group: list[Property] = []
        super().__init__(name)

    @abstractmethod
    def calculate_rent(self, game: Game) -> int:
        """
        Calculates the rent that the player must give to the player who owns the property.
        """
        pass

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
