import unittest

from monocliche.model.Game import Game
from monocliche.model.Player import Player
from monocliche.model.Region import Region


class RegionTest(unittest.TestCase):

    def test_calculate_rent(self):
        player1 = Player("player1")
        player2 = Player("player2")

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region3 = Region("region3", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region4 = Region("region4", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        property_group = [region1, region2, region3, region4]
        region1.property_group = property_group
        region2.property_group = property_group
        region3.property_group = property_group
        region4.property_group = property_group

        game = Game()

        self.assertEqual(0, region1.calculate_rent(game))

        region1.owner = player1
        self.assertEqual(2, region1.calculate_rent(game))

        region2.owner = player1
        self.assertEqual(2, region2.calculate_rent(game))

        region3.owner = player1
        self.assertEqual(2, region3.calculate_rent(game))

        region4.owner = player2
        self.assertEqual(2, region4.calculate_rent(game))

        region4.owner = player1
        self.assertEqual(4, region4.calculate_rent(game))
        self.assertEqual(4, region2.calculate_rent(game))

        region1.structures = 1
        self.assertEqual(4, region1.calculate_rent(game))

        region1.structures = 4
        self.assertEqual(10, region1.calculate_rent(game))

    def test_build_structure(self):
        player = Player("player")

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = region2.property_group = [region1, region2]

        self.assertRaises(Exception, region1.build_structure)

        region1.owner = player
        self.assertRaises(Exception, region1.build_structure)

        region2.owner = player
        region1.build_structure()
        self.assertEqual(1, region1.structures)
        self.assertEqual(0, region2.structures)

        region2.build_structure()
        self.assertEqual(1, region2.structures)

        region1.structures = 4
        # Check the maximum limit of constructions allowed.
        self.assertRaises(Exception, region1.build_structure)

        # Error because the built structures are not proportionate on all properties. region1 = 4 region2 = 2 (1 + new)
        self.assertRaises(Exception, region2.build_structure)

        region1.structures = 1
        region2.build_structure()

        self.assertEqual(2, region2.structures)

        region1.structures = 0
        region2.structures = 0
        region1.mortgaged = True

        # It is not possible to build if a property is mortgaged.
        self.assertRaises(Exception, region1.build_structure)
        self.assertRaises(Exception, region2.build_structure)

    def test_destroy_structure(self):
        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = region2.property_group = [region1, region2]

        # Nothing to destroy.
        self.assertRaises(Exception, region1.destroy_structure)

        region1.structures = 1
        region1.destroy_structure()
        self.assertEqual(0, region1.structures)

        region1.structures = 4
        region2.structures = 3

        # Error because the structures remaining after destruction are not proportionate on all properties.
        self.assertRaises(Exception, region2.destroy_structure)

        region1.structures = 0
        region2.structures = 0
        region1.mortgaged = True

        # If a property is mortgaged, nothing can be destroyed. (There should be no constructions)
        self.assertRaises(Exception, region1.destroy_structure)
        region1.structures = 1

        self.assertRaises(Exception, region1.destroy_structure)
        self.assertRaises(Exception, region2.destroy_structure)

    def test_check_structures_are_proportionate(self):
        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = region2.property_group = [region1, region2]

        self.assertTrue(region1.check_structures_are_proportionate())
        self.assertTrue(region2.check_structures_are_proportionate())

        region1.structures = 1

        self.assertTrue(region1.check_structures_are_proportionate())
        self.assertTrue(region2.check_structures_are_proportionate())

        region2.structures = 1

        self.assertTrue(region1.check_structures_are_proportionate())
        self.assertTrue(region2.check_structures_are_proportionate())

        region1.structures = 4

        self.assertFalse(region1.check_structures_are_proportionate())
        self.assertFalse(region2.check_structures_are_proportionate())

    def test_structure_cost(self):
        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        self.assertEqual(5, region1.structure_cost())

        region1.structures = 2
        self.assertEqual(5, region1.structure_cost())

        region1.structures = 4
        self.assertEqual(10, region1.structure_cost())

    def test_has_construction(self):
        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        self.assertFalse(region1.has_construction())

        region1.structures = 1
        self.assertTrue(region1.has_construction())

    def test_calculate_sales_value(self):
        region1 = Region("region1", price=0, mortgaged_value=5, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        self.assertEqual(5, region1.calculate_sales_value())

        region1.structures = 1

        self.assertEqual(7, region1.calculate_sales_value())

        region1.structures = 3

        self.assertEqual(11, region1.calculate_sales_value())

        region1.structures = 4

        self.assertEqual(16, region1.calculate_sales_value())

    def test_get_number_of_houses(self):
        region1 = Region("region1", price=0, mortgaged_value=5, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.structures = 2

        self.assertEqual(2, region1.get_number_of_houses())

        region1.structures = 4

        self.assertEqual(3, region1.get_number_of_houses())

    def test_get_number_of_hotel(self):
        region1 = Region("region1", price=0, mortgaged_value=5, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.structures = 2

        self.assertEqual(0, region1.get_number_of_hotel())

        region1.structures = 4

        self.assertEqual(1, region1.get_number_of_hotel())


if __name__ == '__main__':
    unittest.main()
