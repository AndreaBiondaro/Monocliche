import unittest

from monocliche.src.LinkedPlayers import LinkedPlayers
from monocliche.src.Player import Player


class LinkedPlayersTest(unittest.TestCase):

    def test_iterate(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()
        self.assertIsNone(next(list_player.iterate()))

        list_player.add(player1)
        list_player.add(player2)

        self.assertEqual(player1.id, next(list_player.iterate()).id)
        self.assertEqual(player2.id, next(list_player.iterate()).id)

    def test_add(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()

        list_player.add(player1)
        self.assertEqual(1, list_player.size)

        list_player.add(player2)
        self.assertEqual(2, list_player.size)

        for x in list_player.iterate():
            self.assertIn(x.id, [player1.id, player2.id])

    def test_remove(self):
        player1 = Player("player1")
        player2 = Player("player2")
        player3 = Player("player3")

        list_player = LinkedPlayers()
        list_player.add(player1)
        list_player.add(player2)

        self.assertEqual(2, list_player.size)

        list_player.remove(player1)
        self.assertEqual(1, list_player.size)
        self.assertEqual(player2.id, next(list_player.iterate()).id)

        list_player.add(player1)
        list_player.remove(player2)
        self.assertEqual(1, list_player.size)
        self.assertEqual(player1.id, next(list_player.iterate()).id)

        list_player.add(player3)
        list_player.remove(player2)
        self.assertEqual(2, list_player.size)
        self.assertEqual(player1.id, next(list_player.iterate()).id)
        self.assertEqual(player3.id, next(list_player.iterate()).id)

    def test_first_player(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()

        self.assertIsNone(list_player.first_player)

        list_player.add(player1)
        self.assertEqual(player1.id, list_player.first_player.id)

        list_player.add(player2)
        self.assertEqual(player1.id, list_player.first_player.id)

    def test_next_player(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()

        self.assertIsNone(list_player.next_player())

        list_player.add(player1)
        self.assertEqual(player1.id, list_player.next_player().id)

        list_player.add(player2)
        self.assertEqual(player2.id, list_player.next_player().id)

    def test_current_player(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()

        self.assertIsNone(list_player.current_player)

        list_player.add(player1)
        self.assertIsNone(list_player.current_player)

        list_player.next_player()
        self.assertEqual(player1.id, list_player.current_player.id)

        list_player.next_player()
        self.assertEqual(player1.id, list_player.current_player.id)

        list_player.add(player2)
        list_player.next_player()
        self.assertEqual(player2.id, list_player.current_player.id)

    def test_extract_non_bankrupt_player(self):
        player1 = Player("player1")
        player2 = Player("player2")

        list_player = LinkedPlayers()
        list_player.add(player1)
        list_player.add(player2)

        self.assertEqual(player1, list_player.extract_non_bankrupt_player())

        player1.bankrupt = True

        self.assertEqual(player2, list_player.extract_non_bankrupt_player())

        player2.bankrupt = True

        self.assertIsNone(list_player.extract_non_bankrupt_player())


if __name__ == '__main__':
    unittest.main()
