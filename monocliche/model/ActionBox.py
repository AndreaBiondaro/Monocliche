from monocliche.model import Game, AbstractAction

from monocliche.model.Box import Box


class ActionBox(Box):
    """
    Represents all the boxes, in which you need to perform some operation.\n
    The boxes in question are:
        - Community chest
        - Income tax
        - Chance
        - Go to jail
        - Luxury tax
    """

    def __init__(self, name: str, action: AbstractAction):
        self.action = action
        super().__init__(name)

    def execute(self, game: Game):
        self.action.execute(game)
