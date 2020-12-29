from monocliche.model.Property import Property


class Region(Property):
    INCOME_MULTIPLIER_FULL_GROUP = 2
    MAXIMUM_NUMBER_OF_CONSTRUCTIONS = 4

    def __init__(self, name: str, price: int, mortgaged_value: int, house_price: int, hotel_price: int, base_rent: int,
                 income_with_house: int, income_with_two_house: int, income_with_three_house: int,
                 income_with_hotel: int):
        self.housePrice = house_price
        self.hotelPrice = hotel_price

        self.base_rent = base_rent
        self.income_with_house = income_with_house
        self.income_with_two_house = income_with_two_house
        self.income_with_three_house = income_with_three_house
        self.income_with_hotel = income_with_hotel

        """Indicates the number of structures built on this box"""
        self.structures = 0
        super().__init__(name, price, mortgaged_value)

    def calculate_rent(self) -> int:
        """
        The calculation of the rent for a territory, is calculated based on how many structures are built
        or if the player owns the whole group of properties.

        The rent is only doubled if the player owns the group and no structures have been built in this box.
        On the other hand, if there is even just one structure, the rent is calculated based on
        the value indicated in the contract.
        """

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

    def build_structure(self):
        """
        Create a new structure on the property.
        The new structure can be built, only if the land is not mortgaged, the player owns the whole group
        or does not exceed the 4 structures already built.
        """
        if not super().mortgaged:
            if super().is_group_owned_by_player():
                if (self.structures + 1) <= Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS:
                    self.structures += 1
                else:
                    # TODO: create a label to use in the front-end that can handle multilanguage
                    raise Exception(
                        f"It is not possible to build more than {Region.MAXIMUM_NUMBER_OF_CONSTRUCTIONS} structures.")
            else:
                # TODO: create a label to use in the front-end that can handle multilanguage
                raise Exception("You don't own all the properties")
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("You cannot build on a mortgaged property.")

    def destroy_structure(self):
        """
        Destroys a property structure.
        The structure can only be destroyed if the property is not mortgaged or does not go to a negative value.
        """
        if not super().mortgaged:
            if (self.structures - 1) >= 0:
                self.structures -= 1
            else:
                # TODO: create a label to use in the front-end that can handle multilanguage
                raise Exception("It is not possible to destroy properties if they no longer exist.")
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to destroy a structure from a mortgaged property.")
