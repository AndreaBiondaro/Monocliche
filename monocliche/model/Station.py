from monocliche.model.Property import Property


class Station(Property):
    INCOME_MULTIPLIER_ONE_STATION = 1
    INCOME_MULTIPLIER_TWO_STATION = 2
    INCOME_MULTIPLIER_THREE_STATION = 4
    INCOME_MULTIPLIER_ALL_STATION = 8

    def __init__(self, name: str, price: int, mortgaged_value: int, base_rent: int):
        self.base_rent = base_rent
        super().__init__(name, price, mortgaged_value)

    def calculate_rent(self) -> int:
        """
        The calculation of the rent for the stations is based on the number of stations owned by the player.
        """
        return {
                   1: Station.INCOME_MULTIPLIER_ONE_STATION,
                   2: Station.INCOME_MULTIPLIER_TWO_STATION,
                   3: Station.INCOME_MULTIPLIER_THREE_STATION,
                   4: Station.INCOME_MULTIPLIER_ALL_STATION
               }.get(super().count_properties_owned_by_player(), 0) * self.base_rent
