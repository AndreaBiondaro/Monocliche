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

    def test_update_game_status(self):
        game = Game()

        game.update_game_status(GameStatus.RUNNING)

        self.assertEqual(GameStatus.RUNNING, game.status)

        game.update_game_status(GameStatus.COMPLETED)

        self.assertEqual(GameStatus.COMPLETED, game.status)

    def test_end_game(self):
        game = Game()

        game.end_game()

        self.assertEqual(GameStatus.COMPLETED, game.status)

    def test_check_game_is_over(self):
        game = Game()

        self.assertFalse(game.check_game_is_over())

        game.status = GameStatus.COMPLETED

        self.assertTrue(game.check_game_is_over())

    def test_extract_non_bankrupt_player(self):
        game = Game()

        player1 = game.add_player("One")
        player2 = game.add_player("Two")

        player1.bankrupt = True

        self.assertEqual(player2, game.players.extract_non_bankrupt_player())

    def test_complete_match(self):
        game = Game()

        player1 = game.add_player("One")
        player2 = game.add_player("Two")

        player1.budget = 100
        player2.budget = 50

        self.assertEqual(player1, game.complete_match())
        self.assertEqual(GameStatus.COMPLETED, game.status)

    def test_roll_dice(self):
        game = Game()

        player1 = game.add_player("One")

        # Initialize the first player.
        game.players.next_player()

        game.roll_dice()
        self.assertEqual(player1.position, game.dice_roll_result.dice_result)

        player1.position = 0

        # Forces the inside counter to have 3 so that on the next roll the player has to go to jail.
        game.dice_roll_result.update_dice_result(1, 1)
        game.dice_roll_result.update_dice_result(1, 1)
        game.dice_roll_result.update_dice_result(1, 1)

        game.roll_dice()

        self.assertTrue(player1.in_jail)


if __name__ == '__main__':
    unittest.main()
