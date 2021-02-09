import unittest

from monocliche.src import Constants

from monocliche.src.Board import Board


class BoardTest(unittest.TestCase):

    def test_initialize_board(self):
        board = Board()

        self.assertIsNone(board.boxes)
        self.assertIsNone(board.community_chest_deck)
        self.assertIsNone(board.chance_deck)

        board.initialize_board()

        self.assertIsNotNone(board.boxes)
        self.assertIsNotNone(board.community_chest_deck)
        self.assertIsNotNone(board.chance_deck)

        self.assertEqual(Constants.NUMBER_OF_BOXES, len(board.boxes))
        self.assertEqual(Constants.NUMBER_OF_COMMUNITY_CHEST_CARDS, len(board.community_chest_deck.cards))
        self.assertEqual(Constants.NUMBER_OF_CHANCE_CARDS, len(board.chance_deck.cards))


if __name__ == '__main__':
    unittest.main()
