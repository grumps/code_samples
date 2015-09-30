__author__ = 'DanielPearl'

import unittest
from c4_view import C4View
from unittest.mock import patch
from io import StringIO

class ShowInstructions(unittest.TestCase):
    """ Tests for printing instructions"""
    # TODO add error messages.

    def setUp(self):
        self.test_view = C4View()
        print(self.shortDescription())

    @patch ('sys.stdout', new_callable=StringIO)
    def test_print_instructions(self,mock_stdout):
        print_statement = \
            ("1. On your turn, drop one of your discs into any slot in the top of "
             "the grid.\n"
             "2. Take turns until one player get four\nof their color discs in a"
             "row -\n"
             "horizontally, vertically, or diagonally\n"
             "3. The first player to 4-in-a-row wins!")
        self.test_view.show_instructions()
        self.assertEqual(print_statement, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()
