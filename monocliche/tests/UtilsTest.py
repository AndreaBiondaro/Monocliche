import unittest

from monocliche.Uitls import Utils


class UtilityTest(unittest.TestCase):

    def test_random_string(self):
        random_string = Utils.random_string(6)

        self.assertEqual(6, len(random_string))


if __name__ == '__main__':
    unittest.main()
