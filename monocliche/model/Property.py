from monocliche.model import Box


class Property(Box):

    def __init__(self, name: str, price: int, mortgaged_value: int):
        self.price = price
        self.mortgaged_value = mortgaged_value
        self.owner = None
        self.mortgaged = False
        self.property_group = []
        super().init(name)
