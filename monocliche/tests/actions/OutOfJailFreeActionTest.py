import unittest

from monocliche.model.Game import Game
from monocliche.model.actions.OutOfJailFreeAction import OutOfJailFreeAction


class OutOfJailFreeActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()

        player1 = game.add_player("One")
        player2 = game.add_player("Two")

        # Initialize the first player.
        game.players.next_player()

        OutOfJailFreeAction().execute(game)

        self.assertTrue(player1.prison_release_card)

        game.players.next_player()

        OutOfJailFreeAction().execute(game)

        self.assertTrue(player1.prison_release_card)
        self.assertTrue(player2.prison_release_card)


if __name__ == '__main__':
    unittest.main()
