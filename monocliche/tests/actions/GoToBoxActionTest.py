import unittest

from monocliche.src.Board import Board
from monocliche.src.Box import Box
from monocliche.src.Game import Game
from monocliche.src.actions.GoToBoxAction import GoToBoxAction


class GoToBoxActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        game.add_player("player1")
        game.players.next_player()
        game.board = Board()

        box1 = Box('box1')
        box2 = Box('box2')
        box3 = Box('box3')
        box4 = Box('box4')
        box5 = Box('box5')
        box6 = Box('box6')

        game.board.boxes = [box1, box2, box3, box4, box5, box6]

        action = GoToBoxAction(box6.id)

        self.assertEqual(0, game.players.current_player.position)

        action.execute(game)

        self.assertEqual(5, game.players.current_player.position)

        action = GoToBoxAction(box3.id)

        action.execute(game)

        self.assertEqual(2, game.players.current_player.position)


if __name__ == '__main__':
    unittest.main
