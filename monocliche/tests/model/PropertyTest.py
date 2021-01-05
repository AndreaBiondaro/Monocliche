import unittest

from monocliche.model.Player import Player
from monocliche.model.Property import Property


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


if __name__ == '__main__':
    unittest.main()
