from monocliche import Constants

from monocliche.model import Region
from monocliche.model.AbstractAction import AbstractAction


class StreetRepairsAction(AbstractAction):
    """
    This class represents the action, in which the player is forced to pay for the repair of the roads,
    based on how many structures he has.
    """

    def __init__(self, cost_per_house, cost_per_hotel):
        self.__cost_per_house = cost_per_house
        self.__cost_per_hotel = cost_per_hotel

    def execute(self, game):
        current_player = game.players.current_player

        total = 0
        for prop in current_player.properties:
            if isinstance(prop, Region):
                total += ((prop.get_number_of_houses() * self.__cost_per_house) + (
                        prop.get_number_of_hotel() * self.__cost_per_hotel))

        if not current_player.update_budget(-total):
            raise Exception(Constants.EXCEPTION_NOT_ENOUGH_MONEY)
