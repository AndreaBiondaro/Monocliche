import unittest

from monocliche.model.Game import Game


class GameTest(unittest.TestCase):

    def test_eq(self):
        game1 = Game()
        game2 = Game()

        self.assertFalse(game1 == game2)

        game1 = game2
        self.assertTrue(game1 == game2)


if __name__ == '__main__':
    unittest.main()
