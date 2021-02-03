from uuid import uuid4
from math import ceil

from monocliche import Constants

from monocliche.model.Exchange import Exchange
from monocliche.model.Property import Property
from monocliche.model.Region import Region


class Player:
    def __init__(self, name: str):
        self.__id = uuid4()
        self.name: str = name
        self.budget: int = 0
        self.properties: list[Property] = []
        self.in_jail = False
        self.my_turn = False
        self.bankrupt = False
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

    def buy_property(self, prop: Property):
        """Buy a new property and update the player's balance."""
        if self.update_budget(-prop.price):
            prop.owner = self
            self.properties.append(prop)
        else:
            raise Exception(Constants.EXCEPTION_NOT_ENOUGH_MONEY)

    def sell_property(self, prop: Property):
        """Sells a property and updates the player's balance."""
        if not prop.check_if_properties_have_buildings():
            self.update_budget(prop.price)
            prop.owner = None
            self.properties.remove(prop)
        else:
            raise Exception(Constants.EXCEPTION_SELL_STRUCTURES_BEFORE_PROCEEDING_WITH_ACTION)

    def build_structure(self, region: Region):
        """
        He builds a new structure on the property.
        To perform this operation the player must have enough money, otherwise it is not possible to continue.
        """
        if isinstance(region, Region):
            # First proceeds with the construction
            region.build_structure()

            # Check if the player has enough money
            if not self.update_budget(-region.structure_cost()):
                # If the player doesn't have enough money, he removes the newly created structure
                region.destroy_structure()
                raise Exception(Constants.EXCEPTION_NOT_ENOUGH_MONEY)
        else:
            raise Exception(Constants.EXCEPTION_PROPERTY_TYPE_NOT_SUPPORT_THE_ACTION)

    def destroy_structure(self, region: Region):
        """
        Destroys a player property structure.
        From this operation, the player receives half the value of the structure from the bank.
        """
        if isinstance(region, Region):
            structure_cost = region.structure_cost()
            try:
                # This is done in a try, in order to be sure that the player's balance is updated
                # only if it is done correctly.
                region.destroy_structure()
                self.update_budget(int(structure_cost / 2))
            finally:
                pass
        else:
            raise Exception(Constants.EXCEPTION_PROPERTY_TYPE_NOT_SUPPORT_THE_ACTION)

    def property_mortgage(self, prop: Property):
        """
        Mortgage a player's property.
        From this operation the player receives the value of the mortgage from the bank and adds it to his balance.
        """

        try:
            # This is done in a try, in order to be sure that the player's balance is updated
            # only if it is done correctly.
            prop.mortgaged = True
            self.update_budget(prop.mortgaged_value)
        finally:
            pass

    def redeem_property_mortgage(self, prop: Property):
        """
        Removes the mortgage from a player's property.
        To remove the mortgage, the value of the mortgage must be paid to the bank plus 10%.
        """

        cost = -(ceil(prop.mortgaged_value * 0.1) + prop.mortgaged_value)

        if self.can_update_budget(cost):
            try:
                prop.mortgaged = False
                self.update_budget(cost)
            finally:
                pass
        else:
            raise Exception(Constants.EXCEPTION_NOT_ENOUGH_MONEY)

    def can_update_budget(self, amount: int) -> bool:
        """
        Returns True if the player's balance after the change is greater than zero, False otherwise.
        """
        return self.budget + amount >= 0

    def update_budget(self, amount: int) -> bool:
        """
        Update the balance that the player has available.
        """

        if self.can_update_budget(amount):
            self.budget = self.budget + amount
            return True
        else:
            return False

    def update_position(self, number_of_boxes: int):
        """
        Update the player's position.

        :param number_of_boxes:indicates the number of squares that the player must skip
        """

        # -1 because the position starts from 0
        last_index = Constants.NUMBER_OF_BOXES - 1

        new_position = self.position + number_of_boxes

        # If it passes the last position of the box, then it is necessary to start from the beginning
        if new_position > last_index:
            new_position -= Constants.NUMBER_OF_BOXES

        self.position = new_position

    def calculate_total_assets(self) -> int:
        """Calculate the assets the player owns. It also takes into account the money of properties and structures."""

        amount = self.budget

        for prop in self.properties:
            amount += prop.calculate_sales_value()

        return amount

    def add_exchange(self, exchange: Exchange):
        if self.exchanges is None:
            self.exchanges = []

        self.exchanges.append(exchange)

    def remove_exchange(self, exchange: Exchange):
        if self.exchanges is not None:
            self.exchanges.remove(exchange)
