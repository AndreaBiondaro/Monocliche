from datetime import datetime

from monocliche.model import Property, Bid


class Auction:

    def __init__(self, start_time: datetime, end_time: datetime, auction_property: Property):
        self.start_time = start_time
        self.end_time = end_time
        self.auction_property = auction_property
        self.offers = []