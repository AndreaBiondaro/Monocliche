import unittest

from monocliche.model.Card import Card
from monocliche.model.Deck import Deck
from monocliche.model.actions.DrawCardAction import DrawCardAction


class DrawCardActionTest(unittest.TestCase):

    def test_execute(self):
        cards = [Card('card1', '', None), Card('card2', '', None)]
        deck = Deck(cards)

        action = DrawCardAction(deck)

        card = action.execute(None)

        self.assertEqual('card1', card.title)

        card = action.execute(None)

        self.assertEqual('card2', card.title)


if __name__ == '__main__':
    unittest.main()
