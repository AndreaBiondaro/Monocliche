import unittest

from monocliche.model.Player import Player
from monocliche.model.Station import Station


class StationTest(unittest.TestCase):

    def test_calculate_rent(self):
        player1 = Player()
        player2 = Player()

        station1 = Station("station1", 0, 0, 25)
        station2 = Station("station2", 0, 0, 25)
        station3 = Station("station3", 0, 0, 25)
        station4 = Station("station4", 0, 0, 25)

        group_property = [station1, station2, station3, station4]
        station1.property_group = group_property
        station2.property_group = group_property
        station3.property_group = group_property
        station4.property_group = group_property

        self.assertEqual(0, station1.calculate_rent())

        station1.owner = player1
        self.assertEqual(25, station1.calculate_rent())
        
        station2.owner = player2
        self.assertEqual(25, station2.calculate_rent())

        self.assertEqual(0, station3.calculate_rent())

        station4.owner = player1
        self.assertEqual(50, station4.calculate_rent())

        station3.owner = player1
        self.assertEqual(100, station3.calculate_rent())
        self.assertEqual(100, station1.calculate_rent())

        station2.owner = player1
        self.assertEqual(200, station1.calculate_rent())


if __name__ == '__main__':
    unittest.main()
