__author__ = 'DanielPearl'

__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model


class MakeBoardTest(unittest.TestCase):
    """Tests make_board"""

    def setUp(self):
        self.model = C4Model()
        print(self.shortDescription())

    def test_make_board(self):
        """test if a board is made correctly."""
        test_board = [['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-'],
                      ['-', '-', '-', '-', '-', '-']]

        self.assertEqual = (test_board, self.model.make_board())

if __name__ == '__main__':
    unittest.main()
