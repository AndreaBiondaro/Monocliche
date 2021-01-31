from monocliche import Constants

from monocliche.model.Property import Property
from monocliche.model import DiceRollResult


class Region(Property):
    INCOME_MULTIPLIER_FULL_GROUP = 2
    MAXIMUM_NUMBER_OF_CONSTRUCTIONS = 4

    def __init__(self, name: str, price: int, mortgaged_value: int, house_price: int, hotel_price: int, base_rent: int,
                 income_with_house: int, income_with_two_house: int, income_with_three_house: int,
                 income_with_hotel: int):
        self.house_price = house_price
        self.hotel_price = hotel_price

        self.base_rent = base_rent
        self.income_with_house = income_with_house
        self.income_with_two_house = income_with_two_house
        self.income_with_three_house = income_with_three_house
        self.income_with_hotel = income_with_hotel

        """Indicates the number of structures built on this box"""
        self.structures = 0
        super().__init__(name, price, mortgaged_value)

    def calculate_rent(self, dice_roll_result: DiceRollResult) -> int:
        """
        The calculation of the rent for a territory, is calculated based on how many structures are built
        or if the player owns the whole group of properties.

        The rent is only doubled if the player owns the group and no structures have been built in this box.
        On the other hand, if there is even just one structure, the rent is calculated based on
        the value indicated in the contract.
        """
        if self.owner is not None:
            if self.structures == 0:
                if super().is_group_owned_by_player():
                    return self.base_rent * Region.INCOME_MULTIPLIER_FULL_GROUP
                else:
                    return self.base_rent
            else:
                return {
                    1: self.income_with_house,
                    2: self.income_with_two_house,
                    3: self.income_with_three_house
                }.get(self.structures, self.income_with_hotel)
        else:
            return 0

    def construction_cost(self) -> int:
        """Returns the cost of building a structure, based on the number of structures present."""

        # if you already have 3 houses, the next one is a hotel, so it returns the cost of a hotel.
        if self.structures < 3:
            return self.house_price
        else:
            return self.hotel_price

    def demolition_cost(self) -> int:
        """Returns the cost of demolishing a structure, based on the number of structures present."""
        if self.structures == Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
            return self.hotel_price
        else:
            return self.house_price

    def build_structure(self):
        """
        Create a new structure on the property.
        The new structure can be built, only if the land is not mortgaged, the player owns the whole group
        or does not exceed the 4 structures already built.
        """
        if not self.mortgaged:
            if super().is_group_owned_by_player():
                if (self.structures + 1) <= Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
                    self.structures += 1
                else:
                    raise Exception(Constants.EXCEPTION_MAXIMUM_CONSTRUCTION_LIMIT)
            else:
                raise Exception(Constants.EXCEPTION_NOT_OWN_ALL_THE_PROPERTY_OF_GROUP)
        else:
            raise Exception(Constants.EXCEPTION_NOT_POSSIBLE_TO_BUILD_ON_MORTGAGE_PROPERTY)

    def destroy_structure(self):
        """
        Destroys a property structure.
        The structure can only be destroyed if the property is not mortgaged or does not go to a negative value.
        """
        if not self.mortgaged:
            if (self.structures - 1) >= 0:
                self.structures -= 1
            else:
                raise Exception(Constants.EXCEPTION_NO_PROPERTIES_TO_DESTROY)
        else:
            raise Exception(Constants.EXCEPTION_NOT_POSSIBLE_TO_DESTROY_ON_MORTGAGE_PROPERTY)
