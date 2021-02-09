from monocliche.src.AbstractAction import AbstractAction


class OutOfJailFreeAction(AbstractAction):
    """
    This class represents the action of free getting out of jail.
    """

    def execute(self, game):
        game.players.current_player.prison_release_card = True
