from uuid import UUID

from monocliche.model import Game
from monocliche.model.AbstractAction import AbstractAction


class GoToBoxAction(AbstractAction):
    """
    This class represents the action in which the player must reach a certain square.
    """

    def __init__(self, id_destination: UUID):
        self._id_destination = id_destination

    def execute(self, game: Game):
        # FIXME: need to use the service to update the player's position !?
        pass
