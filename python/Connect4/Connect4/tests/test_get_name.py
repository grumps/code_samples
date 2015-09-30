__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class GetPlayerTest(unittest.TestCase):
    """Tests """

    def setUp(self):
        self.model = C4Model()
        print(self.shortDescription())
        self.model.set_player("Bob Smith")
        self.model.set_player("Jim Smith")

    def test_get_by_valid_position(self):
        """given player1 or player2 return their name"""
        self.assertEqual("Bob Smith", self.model.get_player(1))

    def test_get_by_valid_position(self):
        """given player1 or player2 return their name"""
        self.assertEqual("Jim Smith", self.model.get_player(2))

    def test_get_by_invalid_position(self):
        """given player1 or player2 return their name"""
        with self.assertRaises(IndexError):
            self.model.get_player(4)

if __name__ == '__main__':
    unittest.main()
