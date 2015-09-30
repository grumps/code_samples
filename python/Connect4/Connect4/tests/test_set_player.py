__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model


class MakeBoardTest(unittest.TestCase):
    """Tests set_player"""

    def setUp(self):
        self.model = C4Model()
        print(self.shortDescription())

    def test_set_name(self):
        """Tests if a player's name is set."""
        self.model.set_player("Bob Smith")
        self.assertEqual("Bob Smith", self.model.players[0])

    def test_set_two_names(self):
        """Tests if a player's name is set."""
        self.model.set_player("Bob Smith")
        self.model.set_player("Jim Smith")
        self.assertEqual(["Bob Smith", "Jim Smith"], self.model.players)