from monocliche.model.Property import Property


class Company(Property):
    INCOME_MULTIPLIER = 4
    INCOME_MULTIPLIER_BOTH_COMPANY = 10

    def __init__(self, name: str):
        super().__init__(name, 2, 1)