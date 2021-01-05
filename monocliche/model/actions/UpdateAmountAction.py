from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class UpdateAmountAction(AbstractAction):
    """
    This class represents an action where the player's budget is updated.
    """

    def __init__(self, amount: int):
        self.__amount = amount

    def execute(self, game: Game):
        # FIXME: need to use the service to update the player's amounts !?
        pass
