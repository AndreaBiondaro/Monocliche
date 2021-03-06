from monocliche.src import Constants

from monocliche.src.actions.GoToBoxAction import GoToBoxAction


class GoToBoxTypeAction(GoToBoxAction):
    """
    this class represents an action in which the player must reach the first square
    of a certain type (station or company).
    """

    def __init__(self, box_type):
        self.__box_type = box_type

    def execute(self, game):
        current_player = game.players.current_player

        boxes = game.board.boxes[current_player.position:]
        boxes.append(game.board.boxes[:current_player.position])

        id_box = None

        # Skip the first one because it is the square where the player is now.
        for box in boxes[1:]:
            if isinstance(box, self.__box_type):
                id_box = box.id
                break

        if id_box is not None:
            super().__init__(id_box)
            super().execute(game)
        else:
            raise Exception(Constants.EXCEPTION_BOX_TYPE_NOT_VALID)
