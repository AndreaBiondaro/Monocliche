import unittest

from monocliche.model.Board import Board
from monocliche.model.Box import Box
from monocliche.model.Game import Game
from monocliche.model.Station import Station
from monocliche.model.actions.GoToBoxTypeAction import GoToBoxTypeAction


class GoToBoxTypeActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        game.add_player("player1")
        game.players.next_player()
        game.board = Board()

        box1 = Box('box1')
        box2 = Box('box2')
        box3 = Box('box3')
        box4 = Station('station', 0, 0, 0)
        box5 = Box('box5')
        box6 = Box('box6')

        game.board.boxes = [box1, box2, box3, box4, box5, box6]

        action = GoToBoxTypeAction(Station)

        self.assertEqual(0, game.players.current_player.position)

        action.execute(game)

        self.assertEqual(3, game.players.current_player.position)


if __name__ == '__main__':
    unittest.main
