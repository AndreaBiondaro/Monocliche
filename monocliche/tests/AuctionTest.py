import unittest
from datetime import datetime

from monocliche.src.Auction import Auction
from monocliche.src.Bid import Bid


class AuctionTest(unittest.TestCase):

    def test_init(self):
        start_time = datetime(2021, 2,
                              9, 19, 49, 0)

        auction = Auction(start_time, None)

        end_time = datetime(2021, 2, 9, 19, 50, 30)

        self.assertEqual(end_time, auction.end_time)

    def test_is_completed(self):
        start_time = datetime(2021, 2,
                              9, 19, 0, 0)

        auction = Auction(start_time, None)

        self.assertTrue(auction.is_completed())

        auction = Auction(datetime.now(), None)
        self.assertFalse(auction.is_completed())

    def test_add_bid(self):
        start_time = datetime(2021, 2,
                              9, 19, 0, 0)

        auction = Auction(start_time, None)

        bid = Bid(None, 0, None)

        self.assertRaises(Exception, auction.add_bid, bid)

        auction = Auction(datetime.now(), None)
        auction.add_bid(bid)

        self.assertEqual(1, len(auction.offers))

    def test_get_winner_bid(self):
        auction = Auction(datetime.now(), None)

        bid = Bid(None, 0, None)

        self.assertIsNone(auction.get_winner_bid())

        auction.offers = [bid]

        self.assertEqual(bid, auction.get_winner_bid())


if __name__ == '__main__':
    unittest.main()
