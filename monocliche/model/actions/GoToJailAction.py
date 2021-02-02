from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class GoToJailAction(AbstractAction):
    def execute(self, game: Game):
        game.players.current_player.in_jail = True
        # TODO: Update player position
