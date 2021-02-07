from monocliche.model import Game, Deck
from monocliche.model.AbstractAction import AbstractAction


class DrawCardAction(AbstractAction):
    """This class is concerned with drawing a card from the deck."""

    def __init__(self, deck: Deck):
        self.__deck = deck

    def execute(self, game: Game):
        return self.__deck.draw_card()
