__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class AddPieceTest(unittest.TestCase):
    """Tests if column is valid or invalid"""

    def setUp(self):
        self.model = C4Model()
        self.model.set_player("Mr. Smith")
        self.model.board = [['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['X', 'X', 'X', 'X', 'X', 'X'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-']]
        print(self.shortDescription())

    def test_add_piece(self):
        """tests adding a piece to an available column"""
        self.assertEqual((3,1), self.model.add_piece(3))

    def test_full_column(self):
        """tests adding a piece to a column that is full."""
        self.assertEqual((None, None), self.model.add_piece(4))


if __name__ == '__main__':
    unittest.main()
