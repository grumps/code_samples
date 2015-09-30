__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from c4_controller import C4Controller
from c4_model import C4Model

class GetPlayerTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        self.model = C4Model()
        print(self.shortDescription())

    @patch('builtins.input', side_effect=["Bob Smith", "Joe Smith"])
    def test_valid_player(self, mock_stdin):
        """test adding valid players to game."""
        self.controller.get_player_names()
        expected_player_list = ["Bob Smith", "Joe Smith"]
        actual_player_list = self.controller.model.players
        self.assertEqual(expected_player_list, actual_player_list)

    @patch('builtins.input', side_effect=["", "", "Why Hello", "Yes"])
    def test_invalid_player(self, mock_stdin):
        """test using invalid player names."""
        self.controller.get_player_names()
        expected_player_list = ["Why Hello", "Yes"]
        actual_player_list = self.controller.model.players
        self.assertEqual(expected_player_list, actual_player_list)

if __name__ == '__main__':
    unittest.main()
