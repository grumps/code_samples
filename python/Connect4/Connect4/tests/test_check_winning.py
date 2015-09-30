__author__ = 'DanielPearl'

import unittest
from c4_controller import C4Controller


class UpdateBoardTest(unittest.TestCase):
    def setUp(self):
        self.controller = C4Controller()
        print(self.shortDescription())

    def test_vert_win(self):
        """tests if it finds a vert win"""
        x = "\033[94m☻\033[0m"
        self.controller.model.board = [[x, x, x, x, '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-']]
        actual = self.controller.check_winner(1,4)
        self.assertTrue(actual)

    def test_horiz_win(self):
        """tests if it finds a horiz win"""
        x = "\033[94m☻\033[0m"
        self.controller.model.board = [[x, '-', '-', '-', '-', '-'],
                                       [x, '-', '-', '-', '-', '-'],
                                       [x, '-', '-', '-', '-', '-'],
                                       [x, '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-']]
        actual = self.controller.check_winner(1,1)
        self.assertTrue(actual)

    def test_diag_win(self):
        """tests if it finds a diag win"""
        x = "\033[94m☻\033[0m"
        self.controller.model.board = [[x, '-', '-', '-', '-', '-'],
                                       ['-', x, '-', '-', '-', '-'],
                                       ['-', '-', x, '-', '-', '-'],
                                       ['-', '-', '-', x, '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-']]
        actual = self.controller.check_winner(1,1)
        self.assertTrue(actual)

    def test_no_win(self):
        """tests if it finds no win"""
        x = "\033[94m☻\033[0m"
        self.controller.model.board = [[x, '-', '-', '-', '-', '-'],
                                       ['-', x, '-', '-', '-', '-'],
                                       ['-', '-', x, '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-'],
                                       ['-', '-', '-', '-', '-', '-']]
        actual = self.controller.check_winner(1,1)
        self.assertFalse(actual)


if __name__ == '__main__':
    unittest.main()
