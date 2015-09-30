__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class GetDiagonalTest(unittest.TestCase):
    """Tests getting the diagonals based on pieces placement"""

    def setUp(self):
        self.model = C4Model()
        self.model.board = [['1', '-', '-', '-', '-', '-'],
                            ['-', 'O', '-', '-', '-', '2'],
                            ['-', '-', 'O', '-', 'O', '2'],
                            ['X', 'X', 'X', 'O', 'X', 'X'],
                            ['-', '-', 'O', 'X', 'O', '-'],
                            ['-', 'O', 'X', '-', '-', 'O'],
                            ['O', 'X', '-', '-', '-', '-']]
        print(self.shortDescription())

    def test_diagonal_all_values_in_grid(self):
        """tests diagonal get of all values within grid"""
        expected = (['1', 'O', 'O', 'O', 'O', 'O'], ['2', 'O', 'O', 'O', 'O', 'O'])
        actual = self.model.get_diagonal(4,4)
        self.assertEqual(expected, actual)

    def test_diagonal_some_values_in_grid(self):
        """tests diagonal of some lists"""
        expected = (['-', '-', 'X', 'X', '-', '-'], ['2', 'X', 'X', 'X', 'X'])
        actual = self.model.get_diagonal(5,4)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
