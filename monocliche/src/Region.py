from monocliche.src import Constants

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

    def has_construction(self) -> bool:
        """Indicates if there are any constructions on the space."""

        return self.structures > 0

    def calculate_sales_value(self) -> int:
        """It indicates the value of selling the territory to the bank."""

        price = super().calculate_sales_value()

        # If there are buildings, you need to add up the value they have.
        if self.has_construction():
            number_house = self.structures
            number_hotel = 0

            if self.structures == Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
                number_hotel = 1
                # Removes the hotel
                number_house -= 1

            price += (int(self.house_price / 2) * number_house) + (int(self.hotel_price / 2) * number_hotel)

        return price

    def structure_cost(self) -> int:
        """Based on the number of structures built, it returns the cost."""

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
        if not self.check_if_properties_are_mortgaged():
            if super().is_group_owned_by_player():
                if (self.structures + 1) <= Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
                    self.structures += 1
                else:
                    raise Exception(Constants.EXCEPTION_MAXIMUM_CONSTRUCTION_LIMIT)

                if not self.check_structures_are_proportionate():
                    self.structures -= 1
                    raise Exception(Constants.EXCEPTION_BUILD_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP)
            else:
                raise Exception(Constants.EXCEPTION_NOT_OWN_ALL_THE_PROPERTY_OF_GROUP)
        else:
            raise Exception(Constants.EXCEPTION_NOT_POSSIBLE_TO_BUILD_ON_MORTGAGE_PROPERTY)

    def destroy_structure(self):
        """
        Destroys a property structure.
        The structure can only be destroyed if the property is not mortgaged or does not go to a negative value.
        """
        if not self.check_if_properties_are_mortgaged():
            if (self.structures - 1) >= 0:
                self.structures -= 1

                if not self.check_structures_are_proportionate():
                    self.structures += 1
                    raise Exception(Constants.EXCEPTION_DESTROY_STRUCTURES_PROPORTIONATE_ON_PROPERTY_GROUP)
            else:
                raise Exception(Constants.EXCEPTION_NO_PROPERTIES_TO_DESTROY)
        else:
            raise Exception(Constants.EXCEPTION_NOT_POSSIBLE_TO_DESTROY_ON_MORTGAGE_PROPERTY)

    def check_structures_are_proportionate(self) -> bool:
        """
        Check that the player is not building/destroying only on one territory.
        At most it is possible to build/destroy only one more structure than the other properties.

        :return true if the player is building/destroying proportionately, false otherwise.
        """

        structures_number = []

        for prop in self.property_group:
            if isinstance(prop, Region):
                structures_number.append(prop.structures)

        min_value = min(structures_number)
        max_value = max(structures_number)

        return max_value - min_value <= 1

    def get_number_of_houses(self) -> int:
        """Returns the number of houses built on this property."""

        number = self.structures

        if number == Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
            number -= 1

        return number

    def get_number_of_hotel(self) -> int:
        """Returns the number of hotel built on this property."""

        number = 0

        if self.structures == Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
            number = 1

        return number
