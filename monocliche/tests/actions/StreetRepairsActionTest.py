import unittest

from monocliche.src.Game import Game
from monocliche.src.Region import Region
from monocliche.src.Station import Station
from monocliche.src.actions.StreetRepairsAction import StreetRepairsAction


class StreetRepairsActionTest(unittest.TestCase):

    def test_execute(self):
        game = Game()
        player = game.add_player("player1")
        player.budget = 100

        game.players.next_player()

        region1 = Region('region1', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        region2 = Region('region2', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        station1 = Station('station1', 0, 0, 0)

        player.properties = [region1, station1, region2]

        action = StreetRepairsAction(10, 20)
        action.execute(game)

        self.assertEqual(100, player.budget)

        region1.structures = 2
        region2.structures = 4

        action = StreetRepairsAction(10, 20)
        action.execute(game)

        self.assertEqual(30, player.budget)

        region1.structures = 2
        region2.structures = 4

        action = StreetRepairsAction(10, 20)

        self.assertRaises(Exception, action.execute, game)


if __name__ == '__main__':
    unittest.main
