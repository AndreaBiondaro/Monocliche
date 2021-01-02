from typing import Any

from monocliche.model import Game
from monocliche.model.actions.GoToBoxAction import GoToBoxAction


class GoToBoxTypeAction(GoToBoxAction):
    """
    this class represents an action in which the player must reach the first square
    of a certain type (station or company).
    """

    def __init__(self, box_type: Any):
        self.__box_type = box_type

    def execute(self, game: Game):
        # TODO: the concept is to search the first box for a certain type, but it is necessary to
        #  start looking in the list from the current position of the player + 1
        id_box = None
        for box in game.board.boxes:
            if type(box) is self.__box_type:
                id_box = box.id
                break

        if id_box is not None:
            super()._id_destination = id_box
            super().execute(game)
        else:
            raise Exception("")
