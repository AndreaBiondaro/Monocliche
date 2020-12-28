from monocliche.model.Property import Property


class Company(Property):
    INCOME_MULTIPLIER = 4
    INCOME_MULTIPLIER_BOTH_COMPANY = 10

    def __init__(self, name: str, price: int, mortgaged_value: int):
        super().__init__(name, price, mortgaged_value)

    def calculate_rent(self) -> int:
        """
        The rent for companies is calculated based on the result of the roll of the dice
        and multiplied by the multiplier.

        The multiplier used is selected based on whether the player owns all companies or not.
        """
        # TODO: Understanding how to get the dice roll
        dice_value = 0
        if super().is_group_owned_by_player():
            return dice_value * Company.INCOME_MULTIPLIER_BOTH_COMPANY
        else:
            return dice_value * Company.INCOME_MULTIPLIER
