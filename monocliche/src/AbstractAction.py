from abc import ABCMeta, abstractmethod


class AbstractAction(metaclass=ABCMeta):
    """
    Abstract class, must be extended by all classes that need to perform an action.
    Actions can be those indicated in the cards (unforeseen events or probabilities), or by certain boxes on the board.
    """

    @abstractmethod
    def execute(self, game):
        """
        Performs an action.
        The "Game" class is passed as an argument in order to have all the necessary information.
        """
        pass
