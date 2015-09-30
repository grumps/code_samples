__author__ = 'DanielPearl'

import unittest
from c4_model import C4Model

class GetColumnTest(unittest.TestCase):
    """Tests if column is valid or invalid"""

    def setUp(self):
        self.model = C4Model()
        print(self.shortDescription())

    def test_valid_column(self):
        """test if we fetch a column, given an column num not index"""
        col = self.model.get_column(3)
        expected_col = ['-', '-', '-', '-', '-', '-']
        self.assertEqual(expected_col, col)
    def test_invalid_column(self):
        """test for an invalid column. give a blank list"""
        col = self.model.get_column(8)
        expected_col = []
        self.assertEqual(expected_col, col)

if __name__ == '__main__':
    unittest.main()
