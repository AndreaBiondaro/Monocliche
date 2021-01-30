from uuid import uuid4
from math import ceil

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
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("You do not have enough money to buy the property.")

    def sell_property(self, prop: Property):
        """Sells a property and updates the player's balance."""
        self.update_budget(prop.price)
        prop.owner = None
        self.properties.remove(prop)

    def build_structure(self, region: Region):
        """
        He builds a new structure on the property.
        To perform this operation the player must have enough money, otherwise it is not possible to continue.
        """
        if isinstance(region, Region):
            structure_cost = -region.construction_cost()
            if self.can_update_budget(structure_cost):
                try:
                    # This is done in a try, in order to be sure that the player's balance is updated
                    # only if it is done correctly.
                    region.build_structure()
                    self.update_budget(structure_cost)
                finally:
                    pass
            else:
                # TODO: create a label to use in the front-end that can handle multilanguage
                raise Exception("You don't have enough money to build a structure on this property.")
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to build structures on this type of property.")

    def destroy_structure(self, region: Region):
        """
        Destroys a player property structure.
        From this operation, the player receives half the value of the structure from the bank.
        """
        if isinstance(region, Region):
            structure_cost = region.demolition_cost()
            try:
                # This is done in a try, in order to be sure that the player's balance is updated
                # only if it is done correctly.
                region.build_structure()
                self.update_budget(int(structure_cost / 2))
            finally:
                pass
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("It is not possible to destroy structures on this type of property.")

    def property_mortgage(self, prop: Property):
        """
        Mortgage a player's property.
        From this operation the player receives the value of the mortgage from the bank and adds it to his balance.
        """
        if not prop.mortgaged:
            # TODO: A land can only be mortgaged if the whole group to whom
            # belongs is devoid of constructions. Where there are buildings, they
            # they must be sold to the Bank which will pay them half of their purchase price
            prop.mortgaged = True
            self.update_budget(prop.mortgaged)
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("The property is already mortgaged.")

    def redeem_property_mortgage(self, prop: Property):
        """
        Removes the mortgage from a player's property.
        To remove the mortgage, the value of the mortgage must be paid to the bank plus 10%.
        """
        if prop.mortgaged:
            prop.mortgaged = False
            self.update_budget(-(ceil((prop.mortgaged_value * 10) / 100) + prop.mortgaged_value))
        else:
            # TODO: create a label to use in the front-end that can handle multilanguage
            raise Exception("The property is not mortgaged")

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
        pass

    def add_exchange(self, exchange: Exchange):
        if self.exchanges is None:
            self.exchanges = []

        self.exchanges.append(exchange)

    def remove_exchange(self, exchange: Exchange):
        if self.exchanges is not None:
            self.exchanges.remove(exchange)
