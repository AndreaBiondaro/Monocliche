from uuid import UUID

from monocliche import Constants

from monocliche.model.AbstractAction import AbstractAction


class GoToBoxAction(AbstractAction):
    """
    This class represents the action in which the player must reach a certain square.
    """

    def __init__(self, id_destination: UUID):
        self.__id_destination = id_destination

    def execute(self, game):
        destination_position = None

        for index, box in enumerate(game.board.boxes):
            if box == self.__id_destination:
                destination_position = index
                break

        if destination_position is not None:
            current_player = game.players.current_player
            current_position = current_player.position

            box_to_skip = 0

            if current_position < destination_position:
                box_to_skip = destination_position - current_position
            else:
                box_to_skip = abs(current_position - Constants.NUMBER_OF_BOXES) + destination_position

            current_player.update_position(box_to_skip)
        else:
            raise Exception(Constants.EXCEPTION_DESTINATION_BOX_NOT_EXISTS)
