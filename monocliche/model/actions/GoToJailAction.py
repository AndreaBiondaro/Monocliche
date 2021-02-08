from monocliche import Constants

from monocliche.model.AbstractAction import AbstractAction
from monocliche.model.actions.GoToBoxAction import GoToBoxAction


class GoToJailAction(AbstractAction):
    def execute(self, game):
        game.players.current_player.in_jail = True

        prison_box = game.board.boxes[Constants.PRISON_CELL_LOCATION]

        action = GoToBoxAction(prison_box.id)
        action.execute(game)
