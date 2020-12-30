import unittest

from monocliche.model.Company import Company
from monocliche.model.Player import Player


class CompanyTest(unittest.TestCase):

    def test_calculate_rent(self):
        player = Player()

        company1 = Company("company1", 0, 0)
        company2 = Company("company2", 0, 0)

        property_group = [company1, company2]
        company1.property_group = property_group
        company2.property_group = property_group

        dice_value = 5

        self.assertEqual(0, company1.calculate_rent())
        company1.owner = player
        self.assertEqual(20, company1.calculate_rent())
        company2.owner = player
        self.assertEqual(50, company2.calculate_rent())

if __name__ == '__main__':
    unittest.main()
