from monocliche.src import Player
from datetime import datetime


class Bid:

    def __init__(self, player: Player, price: int, time: datetime):
        self.player = player
        self.price = price
        self.time = time
