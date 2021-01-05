from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class UpdateAmountEachPlayerAction(AbstractAction):
    """
    This class represents an action where the budget of all players is updated.
    """

    def __init__(self, amount):
        self.__amount = amount

    def execute(self, game: Game):
        # FIXME: need to use the service to update the player's amounts !?
        current_player = game.players.current_player

        counter = 0
        for player in game.players.iterate():
            if player != current_player:
                player.budget -= self.__amount
                counter += 1

        current_player.budget += (counter * self.__amount)
