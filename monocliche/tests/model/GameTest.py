import unittest

from monocliche.model.Game import Game
from monocliche.model.enum.GameStatus import GameStatus


class GameTest(unittest.TestCase):

    def test_add_player(self):
        game = Game()

        player = game.add_player("Name")

        self.assertEqual("Name", player.name)
        self.assertEqual(1, game.players.size)

        game.players = None
        player = game.add_player("Name")

        self.assertIsNotNone(game.players)
        self.assertEqual("Name", player.name)
        self.assertEqual(1, game.players.size)

        player2 = game.add_player("Two")

        self.assertEqual("Two", player2.name)
        self.assertEqual(2, game.players.size)

        game.status = GameStatus.RUNNING

        self.assertRaises(Exception, game.add_player, "Test")

        game.status = GameStatus.COMPLETED

        self.assertRaises(Exception, game.add_player, "Test")

    def test_remove_player(self):
        game = Game()

        player = game.add_player("test")

        game.status = GameStatus.RUNNING

        self.assertRaises(Exception, game.remove_player, player)

        game.status = GameStatus.NEW

        game.remove_player(player)
        self.assertEqual(0, game.players.size)

        self.assertRaises(Exception, game.remove_player)

    def test_passes_turn(self):
        game = Game()

        player1 = game.add_player("One")
        player2 = game.add_player("Two")

        # Necessary to set the starting player, this would be done when the game was started
        game.players.next_player()

        player_turn = game.passes_turn()
        self.assertEqual(player_turn, player2)
        self.assertIs(True, player2.my_turn)

        player_turn = game.passes_turn()
        self.assertEqual(player_turn, player1)
        self.assertIs(False, player2.my_turn)
        self.assertIs(True, player1.my_turn)

        pass

    def test_start_game(self):
        game = Game()

        player = game.add_player("One")

        self.assertIsNone(game.players.current_player)

        game.start_game()
        self.assertIsNotNone(game.players.current_player)
        self.assertEqual(player, game.players.current_player)
        self.assertEqual(GameStatus.RUNNING, game.status)

    def test_check_game_is_over(self):
        # TODO: implements

        pass

    def test_complete_match(self):
        # TODO: implements

        pass


if __name__ == '__main__':
    unittest.main()
