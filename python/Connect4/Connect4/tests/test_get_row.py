__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class GetColumnTest(unittest.TestCase):
    """Tests if column is valid or invalid"""

    def setUp(self):
        self.model = C4Model()
        self.model.board = [['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', 'x', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-']]
        print(self.shortDescription())

    def test_valid_row(self):
        """test if we fetch a column, given an column num not index"""
        row = self.model.get_row(3)
        expected_row = ['-', '-', 'x', '-', '-', '-', '-']
        self.assertEqual(expected_row, row)

    def test_invalid_column(self):
        """test for an invalid column. give a blank list"""
        row = self.model.get_row(7)
        expected_row = None
        self.assertEqual(expected_row, row)

