import unittest

from monocliche.model.Player import Player
from monocliche.model.Property import Property
from monocliche.model.Region import Region


class PropertyTest(unittest.TestCase):

    def test_count_properties_owned_by_player(self):
        player = Player("test")

        prop1 = Property("prop1", 0, 0)
        prop2 = Property("prop2", 0, 0)
        prop2.owner = player
        prop3 = Property("prop3", 0, 0)

        property_group = [prop1, prop2, prop3]

        prop1.property_group = property_group
        prop2.property_group = property_group
        prop3.property_group = property_group

        self.assertEqual(0, prop1.count_properties_owned_by_player())
        self.assertEqual(1, prop2.count_properties_owned_by_player())
        prop1.owner = player
        self.assertEqual(2, prop1.count_properties_owned_by_player())
        self.assertEqual(0, prop3.count_properties_owned_by_player())
        prop3.owner = player
        self.assertEqual(3, prop3.count_properties_owned_by_player())
        prop2.owner = None
        self.assertEqual(2, prop3.count_properties_owned_by_player())
        self.assertEqual(0, prop2.count_properties_owned_by_player())
        prop1.property_group = None
        self.assertRaises(TypeError, prop1.count_properties_owned_by_player)

    def test_is_group_owned_by_player(self):
        player = Player("test")

        prop1 = Property("prop1", 0, 0)
        prop2 = Property("prop2", 0, 0)
        prop2.owner = player
        prop3 = Property("prop3", 0, 0)

        property_group = [prop1, prop2, prop3]

        prop1.property_group = property_group
        prop2.property_group = property_group
        prop3.property_group = property_group

        self.assertFalse(prop1.is_group_owned_by_player())
        self.assertFalse(prop2.is_group_owned_by_player())
        prop1.owner = player
        self.assertFalse(prop1.is_group_owned_by_player())
        prop3.owner = player
        self.assertTrue(prop3.is_group_owned_by_player())
        prop2.owner = None
        self.assertFalse(prop2.is_group_owned_by_player())
        prop1.property_group = None
        self.assertRaises(TypeError, prop1.is_group_owned_by_player)
        prop1.owner = None
        prop1.property_group = []
        self.assertTrue(prop1.is_group_owned_by_player())

    def test_has_construction(self):
        prop1 = Property('prop1', 0, 0)

        self.assertFalse(prop1.has_construction())

    def test_mortgaged(self):
        prop1 = Property('prop1', 0, 0)

        self.assertFalse(prop1.mortgaged)

        prop1.mortgaged = True

        self.assertTrue(prop1.mortgaged)

        prop1.mortgaged = False

        self.assertFalse(prop1.mortgaged)

        self.assertRaises(Exception, prop1.mortgaged, False)

        prop1.mortgaged = True

        self.assertRaises(Exception, prop1.mortgaged, True)

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = [region1]

        region1.owner = Player('Player')

        self.assertFalse(region1.mortgaged)

        region1.mortgaged = True

        self.assertTrue(region1.mortgaged)

        region1.mortgaged = False
        region1.build_structure()

        self.assertRaises(Exception, region1.mortgaged, True)

        region1.destroy_structure()
        region1.mortgaged = True

        self.assertTrue(region1.mortgaged)

    def test_check_if_properties_have_buildings(self):
        player = Player('player')

        prop1 = Property('prop1', 0, 0)
        prop2 = Property('prop2', 0, 0)

        self.assertFalse(prop1.check_if_properties_have_buildings())

        prop1.property_group = prop2.property_group = [prop1, prop2]

        self.assertFalse(prop2.check_if_properties_have_buildings())

        prop1.owner = player
        prop2.owner = player

        self.assertFalse(prop1.check_if_properties_have_buildings())
        self.assertFalse(prop2.check_if_properties_have_buildings())

        region1 = Region("region1", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)
        region2 = Region("region2", price=0, mortgaged_value=0, house_price=5, hotel_price=10, base_rent=2,
                         income_with_house=4, income_with_two_house=6, income_with_three_house=8, income_with_hotel=10)

        region1.property_group = region2.property_group = [region1, region2]

        self.assertFalse(region1.check_if_properties_have_buildings())
        self.assertFalse(region2.check_if_properties_have_buildings())

        region1.owner = player
        region2.owner = player

        self.assertFalse(region1.check_if_properties_have_buildings())
        self.assertFalse(region2.check_if_properties_have_buildings())

        region1.structures = 1

        self.assertTrue(region1.check_if_properties_have_buildings())
        self.assertTrue(region2.check_if_properties_have_buildings())

        region1.structures = 0
        region2.structures = 0

        self.assertFalse(region1.check_if_properties_have_buildings())
        self.assertFalse(region2.check_if_properties_have_buildings())

        region1.structures = 1
        region2.owner = None

        self.assertFalse(region1.check_if_properties_have_buildings())
        self.assertFalse(region2.check_if_properties_have_buildings())


if __name__ == '__main__':
    unittest.main()
