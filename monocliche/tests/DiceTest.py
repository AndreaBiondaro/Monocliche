import unittest

from monocliche.src.Dice import Dice


class DiceTest(unittest.TestCase):

    def test_roll(self):
        dice1 = Dice()

        sides_count = 32
        dice2 = Dice(sides_count)

        for x in range(1000):
            rand1 = dice1.roll()
            rand2 = dice2.roll()
            
            self.assertTrue(1 <= rand1 <= 6)
            self.assertTrue(1 <= rand2 <= sides_count)


if __name__ == '__main__':
    unittest.main()
