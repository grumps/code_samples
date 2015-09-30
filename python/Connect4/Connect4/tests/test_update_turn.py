__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model


class UpdateTurnTest(unittest.TestCase):
    def setUp(self):
        self.model = C4Model()
        print(self.shortDescription())

    def test_player2_turn(self):
        """tests player 2 turn"""
        actual_turn = self.model.update_turn()
        expected_turn = 2
        self.assertEqual(expected_turn, actual_turn)

    def test_player1_turn(self):
        """test's player 1 turn"""
        self.model.current_turn = 2

        expected_turn = 1
        actual_turn = self.model.update_turn()

        self.assertEqual(expected_turn, actual_turn)


if __name__ == '__main__':
    unittest.main()
