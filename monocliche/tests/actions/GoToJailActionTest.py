import unittest

from monocliche import Constants

from monocliche.model.Board import Board
from monocliche.model.Box import Box
from monocliche.model.Game import Game
from monocliche.model.actions.GoToJailAction import GoToJailAction


class GoToJailActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        game.add_player("player1")
        game.players.next_player()
        game.board = Board()
        game.board.boxes = []

        # Populates the list of all boxes
        for i in range(Constants.PRISON_CELL_LOCATION + 1):
            box = Box(str(i))
            game.board.boxes.append(box)

        action = GoToJailAction()

        action.execute(game)

        self.assertTrue(game.players.current_player.in_jail)
        self.assertEqual(Constants.PRISON_CELL_LOCATION, game.players.current_player.position)


if __name__ == '__main__':
    unittest.main
