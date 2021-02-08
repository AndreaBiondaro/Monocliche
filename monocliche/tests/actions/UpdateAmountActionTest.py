import unittest

from monocliche.model.Game import Game
from monocliche.model.actions.UpdateAmountAction import UpdateAmountAction


class UpdateAmountActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        game.add_player("player1")

        game.players.next_player()

        self.assertEqual(0, game.players.current_player.budget)

        action = UpdateAmountAction(100)
        action.execute(game)

        self.assertEqual(100, game.players.current_player.budget)

        action = UpdateAmountAction(-50)
        action.execute(game)

        self.assertEqual(50, game.players.current_player.budget)


if __name__ == '__main__':
    unittest.main
