import unittest

from monocliche.src.Card import Card
from monocliche.src.Deck import Deck


class DeckTest(unittest.TestCase):

    def test_draw_card(self):
        card1 = Card("title1", "", None)
        card2 = Card("title2", "", None)

        deck = Deck([card1, card2])

        card = deck.draw_card()

        self.assertEqual("title1", card.title)
        self.assertEqual(2, len(deck.cards))
        self.assertEqual("title2", deck.cards[0].title)
        self.assertEqual("title1", deck.cards[1].title)


if __name__ == '__main__':
    unittest.main()
