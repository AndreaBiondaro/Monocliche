from monocliche.model.Property import Property


class Region(Property):

    def __init__(self, structures: int, house_price: int, hotel_price: int, income_with_house:int,
                 income_with_two_house: int, income_with_three_house: int, income_with_hotel: int, group_income: int, name: str, price: int, mortgaged_value: int):
        self.structures = structures
        self.housePrice = house_price
        self.hotelPrice = hotel_price
        self.income_with_house = income_with_house
        self.income_with_two_house = income_with_two_house
        self.income_with_three_house = income_with_three_house
        self.income_with_hotel = income_with_hotel
        self.group_income = group_income
        super().__init__(name, price, mortgaged_value)
