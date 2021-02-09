from monocliche.src.AbstractAction import AbstractAction


class UpdatePositionAction(AbstractAction):
    """
    This class represents an action in which it is necessary to change the position
    of a player for certain number of squares forward or backward.
    """

    def __init__(self, position_to_change: int):
        self.__position_to_change = position_to_change

    def execute(self, game):
        game.players.current_player.update_position(self.__position_to_change)
