from monocliche.model import Player
from datetime import datetime


class Bid:

    def __init__(self, player: Player, price: int, time: datetime):
        self._player = player
        self._price = price
        self._time = time

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player: player):
        self._player = player

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        self._price = price

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, time: datetime):
        self._time = time
