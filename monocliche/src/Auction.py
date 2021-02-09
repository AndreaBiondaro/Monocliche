from datetime import datetime, timedelta

from monocliche.src import Constants, Bid


class Auction:

    def __init__(self, start_time: datetime, auction_property):
        self.start_time = start_time
        self.end_time = self.start_time + timedelta(seconds=Constants.AUCTION_DURATION)
        self.auction_property = auction_property
        self.offers: list[Bid] = []

    def add_bid(self, bid: Bid):
        if not self.is_completed():
            self.offers.append(bid)
        else:
            raise Exception(Constants.EXCEPTION_AUCTION_COMPLETED)

    def is_completed(self) -> bool:
        """
        Check if the auction time is up

        :return: True if the auction is complete, False otherwise
        """

        return datetime.now() > self.end_time

    def get_winner_bid(self):
        """Returns the last bid made, which is considered the next bid."""

        if self.offers is not None and len(self.offers) > 0:
            return self.offers[-1]
        else:
            return None
