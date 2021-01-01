import unittest

from monocliche.model.Company import Company
from monocliche.model.Game import Game
from monocliche.model.Player import Player


class CompanyTest(unittest.TestCase):

    def test_calculate_rent(self):
        player = Player("player")

        company1 = Company("company1", 0, 0)
        company2 = Company("company2", 0, 0)

        property_group = [company1, company2]
        company1.property_group = property_group
        company2.property_group = property_group

        game = Game()
        game.dice_roll_result.update_dice_result(3, 2)

        self.assertEqual(0, company1.calculate_rent(game))
        company1.owner = player
        self.assertEqual(20, company1.calculate_rent(game))
        company2.owner = player
        self.assertEqual(50, company2.calculate_rent(game))

        game.dice_roll_result = None
        self.assertRaises(AttributeError, company2.calculate_rent, game)

        game = None
        self.assertRaises(AttributeError, company2.calculate_rent, game)


if __name__ == '__main__':
    unittest.main()
