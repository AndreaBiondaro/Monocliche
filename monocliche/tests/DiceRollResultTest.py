import unittest

from monocliche.model.DiceRollResult import DiceRollResult


class DiceRollResultTest(unittest.TestCase):

    def test_update_dice_result(self):
        dice_result = DiceRollResult()

        dice_result.update_dice_result(1, 2)
        self.assertEqual(3, dice_result.dice_result)
        self.assertEqual(0, dice_result.double_value_counter)

        dice_result.update_dice_result(2, 3)
        self.assertEqual(5, dice_result.dice_result)
        self.assertEqual(0, dice_result.double_value_counter)

        dice_result.update_dice_result(6, 6)
        self.assertEqual(12, dice_result.dice_result)
        self.assertEqual(1, dice_result.double_value_counter)

        dice_result.reset()
        self.assertEqual(0, dice_result.dice_result)
        self.assertEqual(0, dice_result.double_value_counter)


if __name__ == '__main__':
    unittest.main()
