from uuid import uuid4

from monocliche.src import Player, Property


class Exchange:

    def __init__(self, player_from: Player = None, player_to: Player = None, asking_price: int = 0,
                 price_offered: int = 0, required_properties: list[Property] = None,
                 given_properties: list[Property] = None):
        self.__id = uuid4()
        self.player_from: Player = player_from
        self.player_to: Player = player_to
        # Price requested from the player_to
        self.asking_price = asking_price
        # Price offered to the player_from
        self.price_offered = price_offered
        # Property to be given to the player_from
        self.required_properties: list[Property] = required_properties
        # Property to be given to the player_to
        self.given_properties: list[Property] = given_properties

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Exchange):
            return False

        return self.__id == other.__id

    def send_request(self):
        self.player_to.exchanges.append(self)

    def reject_exchange(self):
        self.player_to.exchanges.remove(self)

    def accept_exchange(self):
        """By accepting the trade, player properties and budgets are updated."""

        # The check is not made if there are buildings on the property.
        if self.required_properties is not None:
            for prop in self.required_properties:
                prop.owner = self.player_from
                self.player_from.properties.append(prop)

            self.player_to.properties = [prop for prop in self.player_to.properties if
                                         prop not in self.required_properties]

        if self.given_properties is not None:
            for prop in self.given_properties:
                prop.owner = self.player_to
                self.player_to.properties.append(prop)

            self.player_from.properties = [prop for prop in self.player_from.properties if
                                           prop not in self.given_properties]

        if self.price_offered != 0:
            if not self.player_from.update_budget(-self.price_offered):
                # TODO: The player fails to give the money
                pass
            self.player_to.update_budget(self.price_offered)

        if self.asking_price != 0:
            if not self.player_to.update_budget(-self.asking_price):
                # # TODO: The player fails to give the money
                pass
            self.player_from.update_budget(self.asking_price)

        self.player_to.exchanges.remove(self)
