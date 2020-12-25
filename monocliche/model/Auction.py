from datetime import datetime

from monocliche.model import Property, Bid


class Auction:

    def __init__(self, start_time: datetime, end_time: datetime, auction_property: Property):
        self._start_time = start_time
        self._end_time = end_time
        self._auction_property = auction_property
        self._offers = []

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time: datetime):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time: datetime):
        self._end_time = end_time

    @property
    def auction_property(self):
        return self._auction_property

    @auction_property.setter
    def auction_property(self, auction_property: Property):
        self._auction_property = auction_property

    @property
    def offers(self):
        return self._offers

    def add_bid(self, bid: Bid):
        if self._offers is None:
            self._offers = []

        self._offers.append(bid)
