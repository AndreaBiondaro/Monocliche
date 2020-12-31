from random import randint


class Dice:

    def __init__(self, sides_count: int = 6):
        # we don't want somebody to be able to change the number of sides once the die is created
        self.__sides_count = sides_count

    @property
    def sides_count(self):
        return self.__sides_count

    def roll(self) -> int:
        """
        Rolls a die and returns a number from 1 to the sides count
        """
        return randint(1, self.__sides_count)
