import unittest

from monocliche.src.Exchange import Exchange
from monocliche.src.Player import Player
from monocliche.src.Property import Property


class ExchangeTest(unittest.TestCase):

    def test_send_request(self):
        player_from = Player('player1')
        player_to = Player('player2')

        ex1 = Exchange(player_from, player_to)

        self.assertEqual(0, len(player_to.exchanges))

        ex1.send_request()

        self.assertEqual(1, len(player_to.exchanges))

    def test_reject_exchange(self):
        player_from = Player('player1')
        player_to = Player('player2')

        ex1 = Exchange(player_from, player_to)
        player_to.exchanges = [ex1]

        self.assertEqual(1, len(player_to.exchanges))

        ex1.reject_exchange()

        self.assertEqual(0, len(player_to.exchanges))

    def test_accept_exchange(self):
        player_from = Player('player1')
        player_to = Player('player2')

        prop1 = Property("prop1", 0, 0)
        prop2 = Property("prop2", 0, 0)

        player_to.properties = [prop1]
        player_from.properties = [prop2]
        player_to.budget = 100
        player_from.budget = 50

        ex1 = Exchange(player_from, player_to, 20, 30, [prop1], [prop2])
        player_to.exchanges = [ex1]

        ex1.accept_exchange()

        self.assertEqual(110, player_to.budget)
        self.assertEqual(40, player_from.budget)

        self.assertEqual(prop2, player_to.properties[0])
        self.assertEqual(prop1, player_from.properties[0])


if __name__ == '__main__':
    unittest.main()
