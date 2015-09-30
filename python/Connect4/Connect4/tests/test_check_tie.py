__author__ = 'DanielPearl'

import unittest
from unittest.mock import patch
from c4_controller import C4Controller

class CheckTieTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        self.controller.model.board = \
                [['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['X', 'X', 'X', 'X', 'X', 'X']]
        print(self.shortDescription())

    def test_board_full(self):
        """tests if board is full"""
        actual = self.controller.check_tie()
        self.assertTrue(actual)

    def test_board_not_full(self):
        """Test if a non full board is available"""

        self.controller.model.board[0][0] = '-'
        actual = self.controller.check_tie()
        self.assertFalse(actual)




if __name__ == '__main__':
    unittest.main()
