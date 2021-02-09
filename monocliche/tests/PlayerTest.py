import unittest

from monocliche.src.Player import Player
from monocliche.src.Property import Property
from monocliche.src.Region import Region


class PlayerTest(unittest.TestCase):

    def test_eq(self):
        player1 = Player('player1')
        player2 = Player('player2')

        self.assertFalse(player1 == player2)

        self.assertTrue(player1 == player1)

    def test_buy_property(self):
        player1 = Player('player1')
        player1.budget = 100

        prop1 = Property("prop1", 20, 5)
        prop2 = Property('prop2', 90, 5)

        player1.buy_property(prop1)

        self.assertEqual(80, player1.budget)
        self.assertEqual(player1, prop1.owner)
        self.assertEqual(1, len(player1.properties))

        self.assertRaises(Exception, player1.buy_property, prop2)

        player1.budget = 90
        player1.buy_property(prop2)

        self.assertEqual(0, player1.budget)
        self.assertEqual(player1, prop2.owner)
        self.assertEqual(2, len(player1.properties))

    def test_sell_property(self):
        player1 = Player('player1')

        prop1 = Property("prop1", 20, 5)

        prop1.owner = player1
        player1.properties = [prop1]

        player1.sell_property(prop1)

        self.assertEqual(20, player1.budget)
        self.assertIsNone(prop1.owner)
        self.assertEqual(0, len(player1.properties))

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = [region1]
        region1.owner = player1
        player1.properties = [region1]
        region1.structures = 1

        self.assertRaises(Exception, player1.sell_property, region1)

        region1.structures = 0
        region1.property_group = region2.property_group = [region1, region2]
        region1.owner = region2.owner = player1
        player1.properties = [region1, region2]

        player1.sell_property(region2)

        self.assertEqual(region1, player1.properties[0])

    def test_build_structure(self):
        player1 = Player('player1')

        prop1 = Property("prop1", 20, 5)

        self.assertRaises(Exception, player1.build_structure, prop1)

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = [region1]
        region1.owner = player1

        self.assertRaises(Exception, player1.build_structure, region1)
        self.assertEqual(0, region1.structures)

        player1.budget = 100
        player1.build_structure(region1)

        self.assertEqual(1, region1.structures)
        self.assertEqual(95, player1.budget)

    def test_destroy_structure(self):
        player1 = Player('player1')

        prop1 = Property("prop1", 20, 5)

        self.assertRaises(Exception, player1.destroy_structure, prop1)

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = [region1]
        region1.owner = player1

        self.assertRaises(Exception, player1.destroy_structure, region1)

        region1.structures = 1

        player1.destroy_structure(region1)

        self.assertEqual(0, region1.structures)
        self.assertEqual(2, player1.budget)

        region1.structures = 4
        player1.budget = 0

        player1.destroy_structure(region1)

        self.assertEqual(3, region1.structures)
        self.assertEqual(5, player1.budget)

        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2.owner = player1

        region2.property_group = region1.property_group = [region1, region2]

        region1.structures = 3
        region2.structures = 1

        player1.budget = 0

        self.assertRaises(Exception, player1.destroy_structure, region2)
        self.assertEqual(0, player1.budget)

    def test_property_mortgage(self):
        player1 = Player('player1')

        prop1 = Property("prop1", 20, 5)
        prop1.owner = player1

        player1.property_mortgage(prop1)

        self.assertTrue(prop1.mortgaged)
        self.assertEqual(5, player1.budget)

    def test_redeem_property_mortgage(self):
        player1 = Player('player1')

        prop1 = Property("prop1", 20, 5)
        prop1.owner = player1
        prop1.mortgaged = True

        self.assertRaises(Exception, player1.redeem_property_mortgage, prop1)

        player1.budget = 10

        player1.redeem_property_mortgage(prop1)

        self.assertFalse(prop1.mortgaged)
        # Cost to redeem the mortgage is: mortgage value + 10% -->
        # (5 + 10%) = 5.5 --> 6 (We cannot have numbers with commas and round up)
        self.assertEqual(4, player1.budget)

    def test_can_update_budget(self):
        player1 = Player('player1')

        self.assertFalse(player1.can_update_budget(-1))
        self.assertTrue(player1.can_update_budget(1))

        player1.budget = 10
        self.assertTrue(player1.can_update_budget(-1))

        self.assertEqual(10, player1.budget)

    def test_update_budget(self):
        player = Player('player')

        self.assertFalse(player.update_budget(-1))
        self.assertEqual(0, player.budget)

        self.assertTrue(player.update_budget(1))
        self.assertEqual(1, player.budget)

        self.assertTrue(player.update_budget(-1))
        self.assertEqual(0, player.budget)

    def test_update_position(self):
        player = Player('player')

        player.update_position(3)

        self.assertEqual(3, player.position)

        player.position = 37

        player.update_position(5)

        self.assertEqual(2, player.position)

    def test_calculate_total_assets(self):
        player = Player('player')
        player.budget = 500

        self.assertEqual(500, player.calculate_total_assets())

        prop1 = Property("prop1", 20, 5)
        prop1.owner = player
        player.properties = [prop1]

        self.assertEqual(505, player.calculate_total_assets())


if __name__ == '__main__':
    unittest.main()
