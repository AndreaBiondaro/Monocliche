from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class OutOfJailFreeAction(AbstractAction):
    """
    This class represents the action of free getting out of jail.
    """

    def execute(self, game: Game):
        game.players.current_player.prison_release_card = True
