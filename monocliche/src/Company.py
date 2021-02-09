from monocliche.src.Property import Property
from monocliche.src import DiceRollResult


class Company(Property):
    INCOME_MULTIPLIER = 4
    INCOME_MULTIPLIER_BOTH_COMPANY = 10

    def __init__(self, name: str, price: int, mortgaged_value: int):
        super().__init__(name, price, mortgaged_value)

    def calculate_rent(self, dice_roll_result: DiceRollResult) -> int:
        """
        The rent for companies is calculated based on the result of the roll of the dice
        and multiplied by the multiplier.

        The multiplier used is selected based on whether the player owns all companies or not.
        """
        dice_value = dice_roll_result.dice_roll_result.dice_result
        if self.owner is not None:
            if super().is_group_owned_by_player():
                return dice_value * Company.INCOME_MULTIPLIER_BOTH_COMPANY
            else:
                return dice_value * Company.INCOME_MULTIPLIER
        else:
            return 0
