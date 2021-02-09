import unittest

from monocliche.src.Game import Game
from monocliche.src.actions.UpdatePositionAction import UpdatePositionAction


class UpdatePositionActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        game.add_player("player1")
        game.players.next_player()

        self.assertEqual(0, game.players.current_player.position)

        action = UpdatePositionAction(10)
        action.execute(game)

        self.assertEqual(10, game.players.current_player.position)

        action = UpdatePositionAction(-3)
        action.execute(game)

        self.assertEqual(7, game.players.current_player.position)


if __name__ == '__main__':
    unittest.main
