from monocliche.model.Property import Property


class Station(Property):
    INCOME_ONE_STATION = 1
    INCOME_TWO_STATION = 2
    INCOME_THREE_STATION = 4
    INCOME_ALL_STATION = 8

    # TODO INSERIRE COSTANTE COSTO/IPOTECA STAZIONE
    def __init__(self, name: str):
        super().__init__(name, 2, 1)
