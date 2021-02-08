import unittest

from monocliche.model.Game import Game
from monocliche.model.actions.UpdateAmountEachPlayerAction import UpdateAmountEachPlayerAction


class UpdateAmountEachPlayerActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        player1 = game.add_player("player1")
        player2 = game.add_player("player2")
        player3 = game.add_player("player3")
        game.players.next_player()

        player1.budget = 50
        player2.budget = 50
        player3.budget = 50

        action = UpdateAmountEachPlayerAction(10)
        action.execute(game)

        self.assertEqual(70, game.players.current_player.budget)
        self.assertEqual(40, player2.budget)
        self.assertEqual(40, player3.budget)

        action = UpdateAmountEachPlayerAction(-20)
        action.execute(game)

        self.assertEqual(30, game.players.current_player.budget)
        self.assertEqual(60, player2.budget)
        self.assertEqual(60, player3.budget)


if __name__ == '__main__':
    unittest.main
