class DiceRollResult:
    """
    Class to keep track of the result of the roll of the dice.
    """

    def __init__(self):
        self.__dice_result = 0
        # It is used to keep track of how many times an equal number has been rolled
        self.__double_value_counter = 0

    @property
    def dice_result(self):
        return self.__dice_result

    @property
    def double_value_counter(self):
        return self.__double_value_counter

    def __increase_double_value_counter(self):
        self.__double_value_counter += 1

    def update_dice_result(self, first_result: int, second_result: int):
        """
        Update the value of the dice result, and if the two numbers are equal it increases the double value counter.
        """
        self.__dice_result = first_result + second_result

        if first_result == second_result:
            self.__increase_double_value_counter()

    def reset(self):
        self.__dice_result = 0
        self.__double_value_counter = 0
