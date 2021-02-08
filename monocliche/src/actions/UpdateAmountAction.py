from monocliche.src import Constants

from monocliche.model.AbstractAction import AbstractAction


class UpdateAmountAction(AbstractAction):
    """
    This class represents an action where the player's budget is updated.
    """

    def __init__(self, amount: int):
        self.__amount = amount

    def execute(self, game):
        if not game.players.current_player.update_budget(self.__amount):
            raise Exception(Constants.EXCEPTION_NOT_ENOUGH_MONEY)
