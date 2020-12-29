from monocliche.model import Game, AbstractAction


class ActionBox:
    """
    Represents all the boxes, in which you need to perform some operation.\n
    The boxes in question are:
        - Community chest
        - Income tax
        - Chance
        - Go to jail
        - Luxury tax
    """

    def __init__(self, action: AbstractAction):
        self.action = action

    def execute(self, game: Game):
        self.action.execute(game)
