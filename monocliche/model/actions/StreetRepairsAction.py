from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class StreetRepairsAction(AbstractAction):
    """
    This class represents the action, in which the player is forced to pay for the repair of the roads,
    based on how many structures he has.
    """

    def __init__(self, cost_per_house, cost_per_hotel):
        self.__cost_per_house = cost_per_house
        self.__cost_per_hotel = cost_per_hotel

    def execute(self, game: Game):
        # FIXME: need to use the service to update the player's amounts !?
        pass
